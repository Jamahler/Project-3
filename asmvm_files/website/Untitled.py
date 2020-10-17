% pip install Flask-PyMongo
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    recipe = mongo.db