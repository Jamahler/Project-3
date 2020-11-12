from flask import Flask, render_template, request
import requests
import pymongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request
from bson import json_util

app = Flask(__name__)

# app.config['MONGO_URI'] = "mongodb://localhost:27017/Dodecagon"
# mongo = PyMongo(app)
# from pymongo import MongoClient
# client = MongoClient('mongodb://localhost:27017/')
# db = client['Dodecagon']
# recipes_collection = db.recipes

# Suggested format to connect with MongoDB 
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['Dodecagon']
recipes_collection = db.recipes
wines_collection = db.wines


# This route connects with mongo db and gets all recipes
@app.route('/recipe')
def getrecipe():
    # wines_data = [x for x in wines_collection.find()]
    recipe = recipes_collection.find()
    # resp = dumps(wines[2]['wine'])
    # resp = dumps(wines)
    # resp = json_util.dumps(wine for wine in wines)

    resp = json_util.dumps(recipe)
 
    # return render_template('wines.html', wines=resp)    
    return resp


# This route returns a loop of the wine list, wish to use this for dynamic dropdown
# However, when we render to template, we only get one
# character at a time, not the full wine name
@app.route('/winess')
def winelist():
    # wines_data = [x for x in wines_collection.find()]
    wines = wines_collection.find()
    

    # for w in len(wines):
    #     x = wines[w]['wine']      
    #     print(x)
    # resp = dumps(wines[2]['wine'])
    # resp = json_util.dumps(wines)
    resp = json_util.dumps(wine for wine in wines)
    # resp = json_util.dumps({'wine':wines[1]['wine']})

    # print(wines)
    return render_template('wine_dropdown.html', wines=resp)    
    # return resp

# THIS IS THE GOOD JSON ROUTE DO NOT DELETE!
# Alternative format to get wine information, as all previous attempts only
# loop through each character in the wine names when we render to template
@app.route('/json-wines', methods=['GET', 'POST'])
def get_all_wines():
  wines = wines_collection.find()
  output = []

  for w in wines:
    output.append({'wine':w['wine'], 'pairing':w['pairing'], 'description':w['description']})
  print(output)
  wines_json = jsonify(output)
  return wines_json
  
#   return render_template('wines.html', wines=list)  
#   return jsonify({'result': output[2]["wine"]})
#   print(output)
#   return jsonify({'result': output})
#   return jsonify(list_of_dictionaries)

## Additional routes we tested to try and loop through wines or recipes in MongoDB


# @app.route("/")
# def index():
#     meal = mongo.db.recipes.find_one()
#     return render_template(index.html, meal=meal)

# @app.route('/dish/<dish>')
# def  dish(dish):
#     meal = recipes_collection.find({'Title':dish})
#     print(meal)
#     resp = dumps(meal)
#     return resp

# @app.route('/dish')
# def dish():
#     meal = recipes_collection.find_one({'Spoon_ID': "920049.0"})
#     # return f'<h1>Recipe: {meal["Title"]}</h1><h2>Percent_Fat: {meal["Percent_Fat"]}</h2><h3>Summary: {meal["Summary"]}</h3>'
#     return meal["Title"]


# @app.route('/recipes')
# def recipes():
#     recipes = mongo.db.recipes.find({},{'Title':1})
#     resp = dumps(recipes)
#     return resp

# @app.route('/wines')
# def wines():
#     wines = mongo.db.wines.find({},{'wine':1})
#     resp = dumps(wines)
#     return resp

# @app.route('/wine')
# def wine():
#     wine = wines_collection.find({},{'wine':1})
#     pairing = wines_collection.find({},{'pairing':1})
#     # return f'<h1>Recipe: {meal["Title"]}</h1><h2>Percent_Fat: {meal["Percent_Fat"]}</h2><h3>Summary: {meal["Summary"]}</h3>'
#     resp = dumps(wine, pairing)
#     return resp

# @app.route('/getwine', methods = ['POST'])
# def getwine():
#     wine = request.form['wine']
#     if wine:
#         wine_list = wines_collection.wines.tolist()
#         return jsonify({'winesList': wine })


# @app.route('/wines/', methods=['GET'])
# def get_one_wine():
 
# #   w = wines_collection.find_one({'wine':wine})
#   if w:
#     output = {'wine' : w['wine'], 'description' : w['description']}
#   else:
#     output = "No such name"
#   return jsonify({'result' : output})


# @app.route('/wines')
# def winelist():
#     # wines_data = [x for x in wines_collection.find()]
#     wines = wines_collection.find()
#     # resp = dumps(wines[2]['wine'])
#     # resp = dumps(wines)
#     resp = dumps([wine['wine'] for wine in wines])
    
#     return render_template('wines.html', wines=resp)    
#     # return resp



if __name__ == "__main__":
    app.run(debug=True)

