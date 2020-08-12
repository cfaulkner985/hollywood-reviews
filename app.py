# IMPORTTING MODULES THAT WE WILL USE TO RUN THE SITE
import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if os.path.exists("env.py"):
    import env

# LINKING FLASK TO MY MONGO DB SITE WITH THE
# DATABASE NAME AND THE URI OF THE DATABASE AND SECRET KEY
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


# CONNECTING MONGO TO PYMONGO
mongo = PyMongo(app)

# ---------- REVIEWS ---------- #
# SETTING INDEX.HTML MY OPENING PAGE FOR THE SITE
# LINKING THE USER INFORMATION TABLE IN MONGO DB TO MY INDEX.HTML PAGE


@app.route('/')
@app.route('/insert_review')
def add_review():
    return render_template(
        "index.html",
        user_information=mongo.db.user_information.find())

# LINKING THE ADDED REVIEWS TABLE IN MONGO DB TO MY REVIEWS.HTML PAGE


@app.route('/get_reviews')
def get_reviews():
    return render_template(
        "reviews.html",
        added_reviews=mongo.db.added_reviews.find())


# THIS CODE BRINGS THE INFORMATION I INSERT INTO INDEX.HTML TO REVIEWS.HTML
# USING THE SUMBIT BUTTON IT ALSO SAVES THE INFORMATION INTO THE ADDED REVIEWS
# TABLE IN MONGO DB


@app.route('/add_reviews', methods=['POST'])
def add_reviews():
    added_reviews = mongo.db.added_reviews
    added_reviews.insert_one(request.form.to_dict())
    return redirect(url_for('get_reviews'))


# CREATED EDIT_REWIEWS.HTML SO I CAN EDIT REVIEWS CLICKING ON THE EDIT BUTTON
# ONCE EDITED IT WILL AMMEND IN THE REVIEWS.HTML AND MONGO DB TABLE """


@app.route('/edit_reviews/<reviews_id>')
def edit_reviews(reviews_id):
    the_review = mongo.db.added_reviews.find_one({"_id": ObjectId(reviews_id)})
    all_reviews = mongo.db.added_reviews.find()
    return render_template('edit_reviews.html', reviews=the_review,
                           added_reviews=all_reviews)


# THIS CODE ALLOWS ME TO DELETE REVIEWS CLICKING ON THE DELETE BUTTON
# ONCE DELETED IT WILL REMOVE FROM THE REVIEWS.HTML AND MONGO DB TABLE


@app.route('/delete_reviews/<reviews_id>')
def delete_reviews(reviews_id):
    mongo.db.added_reviews.remove({'_id': ObjectId(reviews_id)})
    return redirect(url_for('get_reviews'))


# THIS CODE IS LINKED TO THE EDIT BUTTON ON THE EDIT_REVIEWS.HTML
# IT UPDATES THE MONGO DB TABLE WHICH THEN UPDATES THE REVIEW LEFT
# I CAN UPDATE THE HEADING WHICH ARE LISTED BELOW


@app.route('/update_reviews/<reviews_id>', methods=["POST"])
def update_reviews(reviews_id):
    added_reviews = mongo.db.added_reviews
    added_reviews.update({'_id': ObjectId(reviews_id)},
                         {
        'movie_reviewed': request.form.get('movie_reviewed'),
        'date_reviewed': request.form.get('date_reviewed'),
        'first_name': request.form.get('first_name'),
        'last_name': request.form.get('last_name'),
        'country': request.form.get('country'),
        'email': request.form.get('email'),
        'rating': request.form.get('rating'),
        'thoughts': request.form.get('thoughts')
    })
    return redirect(url_for('get_reviews'))

# ---------- MOVIES ---------- #
# LINKING THE MOVIE INFORMATION TABLE IN MONGO DB TO MY MOVIES.HTML PAGE


@ app.route('/get_movies')
def get_movies():
    return render_template(
        "movies.html",
        movie_information=mongo.db.movie_information.find())


# CREATED ADD_MOVIES.HTML SO I CAN ADD MOVIES CLICKING ON THE ADD
# MOVIES BUTTON ONCE ADDED IT WILL BE INSERTED IN THE MOVIES.HTML AND
# MONGO DB TABLE """


@app.route('/insert_movie', methods=['POST'])
def insert_movie():
    if request.method == "POST":
        info = {
            'title': request.form.get('title'),
            'imdb': request.form.get('imdb'),
            'tomato': request.form.get('tomato'),
            'year': request.form.get('year'),
            'runtime': request.form.get('runtime'),
            'actors': request.form.get('actors'),
            'director': request.form.get('director'),
            'genres': request.form.get('genres'),
            'plot': request.form.get('plot')
        }
        mongo.db.movie_information.insert_one(info)
        return redirect(url_for("get_movies"))

# LINKING THE MOVIE INFORMATION TABLE IN MONGO DB TO MY ADD_MOVIES.HTML PAGE


@app.route('/add_movie')
def add_movie():
    return render_template('add_movies.html')


# USING THE ENVIRON OBJECT TO GET THE IP AND PORT SETTING
# DEBUG TO TRUE SO CHANGES CAN BE PICKED UP IN THE BROWSER
# ALSO PRODUCRS DEBUG STATEMENTS IF NEEDED """
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
