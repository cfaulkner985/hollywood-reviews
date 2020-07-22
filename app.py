import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'movie_reviews'
app.config["MONGO_URI"] = 'mongodb+srv://cfaulkner985:mongoDB123@myfirstcluster.kyuch.mongodb.net/movie_reviews?retryWrites=true&w=majority'


mongo = PyMongo(app)


@app.route('/')
@app.route('/add_review')
def add_review():
    return render_template("user.html", user_information=mongo.db.user_information.find())


@app.route('/get_movies')
def get_movies():
    return render_template("movies.html", movie_information=mongo.db.movie_information.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
