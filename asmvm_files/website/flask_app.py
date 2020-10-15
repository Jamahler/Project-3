from flask import Flask, render_template, request

import requests

from flask_pymongo import PyMongo

from bson.json_util import dumps

from bson.objectid import ObjectId

from flask import jsonify, request

from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# app.secret_key = "secretkey"

app.config['MONGO_URI'] = "mongodb://localhost:27017/Dodecagon"
mongo = PyMongo(app)
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['Dodecagon']
recipes_collection = db.recipes

@app.route("/")
def index():
    meal = mongo.db.recipes.find_one()
    return render_template(index.html, meal=meal)

# @app.route('/dish/<dish>')
# def  dish():
#     meal = mongo.db.recipes.findOne({},{'Title':dish})
#     resp = dumps(dish)
#     return resp

@app.route('/dish')
def dish():
    meal = recipes_collection.find_one({'Spoon_ID': "920049.0"})
    # return f'<h1>Recipe: {meal["Title"]}</h1><h2>Percent_Fat: {meal["Percent_Fat"]}</h2><h3>Summary: {meal["Summary"]}</h3>'
    return meal["Title"]
@app.route('/recipes')
def recipes():
    recipes = mongo.db.recipes.find({},{'Title':1})
    resp = dumps(recipes)
    return resp



if __name__ == "__main__":
    app.run(debug=True)


# if __name__ == '__main__':
#   app.run()