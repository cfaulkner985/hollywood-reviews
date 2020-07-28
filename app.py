# IMPORTTING MODULES THAT WE WILL USE TO RUN THE SITE
import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# LINKING FLASK TO MY MONGO DB SITE WITH THE
# DATABASE NAME AND THE URI OF THE DATABASE
app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'movie_reviews'
app.config["MONGO_URI"] = 'mongodb+srv://cfaulkner985:mongoDB123@myfirstcluster.kyuch.mongodb.net/movie_reviews?retryWrites=true&w=majority'

# CONNECTING MONGO TO PYMONGO
mongo = PyMongo(app)

# SETTING USER.HTML MY OPENING PAGE FOR THE SITE
# LINKING THE USER INFORMATION TABLE IN MONGO DB TO MY USER.HTML PAGE
@app.route('/')
@app.route('/insert_review')
def add_review():
    return render_template("user.html", user_information=mongo.db.user_information.find())

# LINKING THE ADDED REVIEWS TABLE IN MONGO DB TO MY REVIEWS.HTML PAGE
@app.route('/get_reviews')
def get_reviews():
    return render_template("reviews.html", added_reviews=mongo.db.added_reviews.find())

# THIS CODE BRINGS THE INFORMATION I INSERT INTO USER.HTML TO REVIEWS.HTML
# USING THE SUMBIT BUTTON
# IT ALSO SAVES THE INFORMATION INTO THE ADDED REVIEWS TABLE IN MONGO DB
@app.route('/add_reviews', methods=['POST'])
def add_reviews():
    added_reviews = mongo.db.added_reviews
    added_reviews.insert_one(request.form.to_dict())
    return redirect(url_for('get_reviews'))

# LINKING THE MOVIE INFORMATION TABLE IN MONGO DB TO MY MOVIES.HTML PAGE
@app.route('/get_movies')
def get_movies():
    return render_template("movies.html", movie_information=mongo.db.movie_information.find())

# CREATED EDIT_REWIEWS.HTML SO I CAN EDIT REVIEWS CLICKING ON THE EDIT BUTTON
# BESIDE EACH REVIEW THAT IS LEFT VIA THE ADD REVIEWS PAGE
@app.route('/edit_reviews/<reviews_id>')
def edit_reviews(reviews_id):
    the_review =  mongo.db.added_reviews.find_one({"_id": ObjectId(reviews_id)})
    all_reviews = mongo.db.added_reviews.find()
    return render_template('edit_reviews.html', reviews=the_review,
                           added_reviews=all_reviews)

# USING THE ENVIRON OBJECT TO GET THE IP AND PORT
# SETTING DEBUG TO TRUE SO CHANGES CAN BE PICKED UP IN THE BROWSER
# ALSO PRODUCRS DEBUG STATEMENTS IF NEEDED
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
