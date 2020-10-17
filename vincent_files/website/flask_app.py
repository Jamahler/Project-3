from flask import Flask, render_template, request
import requests
import pymongo
# from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from bson import json_util



app = Flask(__name__)

# app.secret_key = "secretkey"

# app.config['MONGO_URI'] = "mongodb://localhost:27017/Dodecagon"
# mongo = PyMongo(app)
# from pymongo import MongoClient
# client = MongoClient('mongodb://localhost:27017/')
# db = client['Dodecagon']
# recipes_collection = db.recipes

from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['Dodecagon']
recipes_collection = db.recipes
wines_collection = db.wines

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

# This route returns a loop of the wine list
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
    #return render_template('wine_dropdown.html', wines=resp)    
    return resp

# THIS IS THE GOOD JSON ROUTE DO NOT DELETE!!!
@app.route('/json-wines', methods=['GET', 'POST'])
def get_all_wines():
  wines = wines_collection.find()
  output = []

  for w in wines_collection.find():
    output.append({'wine':w['wine'], 'pairing':w['pairing'], 'description':w['description']})
  print(output)
  wines_json = jsonify(output)
  return wines_json

  
#   keys = [
#       'wine',
#       'pairing',
#       'description'
#   ]
#   list_of_dictionaries = [dict(zip(keys, wine)) for wine in wines]
  
#   print (list_of_dictionaries)  
  
   
#   return render_template('wines.html', wines=list)  
#   return jsonify({'result': output[2]["wine"]})
#   print(output)
#   return jsonify({'result': output})
#   return jsonify(list_of_dictionaries)


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

# @app.route('/star/', methods=['GET'])
# def get_one_star(name):
  
#   s = star.find_one({'name' : name})
#   if s:
#     output = {'name' : s['name'], 'distance' : s['distance']}
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


@app.route('/recipe')
def getrecipe():
    # wines_data = [x for x in wines_collection.find()]
    recipe = recipes_collection.find()
    # resp = dumps(wines[2]['wine'])
    # resp = dumps(wines)
    # resp = json_util.dumps(wine for wine in wines)

    resp = json_util.dumps(recipe[1])
 
    # return render_template('wines.html', wines=resp)    
    return resp


if __name__ == "__main__":
    app.run(debug=True)


# if __name__ == '__main__':
#   app.run()