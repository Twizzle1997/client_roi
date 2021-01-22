from config import ressources, db_access
from flask import Flask, jsonify
from config.db_access import DatabaseManager as db
import json
import requests
from bson.json_util import dumps
from config.ressources import *

app = Flask(__name__)

@app.route("/")
def hello():
    return {"welcome_message": "World"}


@app.route("/api/request/<name>")
def route_request(name: str):

    content = json.loads(dumps(db.getInstance().get_country_by_name(name)))
    return content

@app.route("/api/add/<name>")
def  route_add(name:str):

    content = json.loads(dumps(db.getInstance().set_country(name)))
    return content

@app.route("/api/remove/<name>")
def  route_remove(name:str):

    content = json.loads(dumps(db.getInstance().delete_country_by_name(name)))
    return content

# @app.route("/api/update/<name><couple>")
# def  route_edit(name:str, couple:dict):

#     content = json.loads(dumps(db.getInstance().update_country_by_name(name, couple)))
#     return content

@app.route("/api/class")
def  route_categorize():

    content = json.loads(dumps(db.getInstance().get_countries_class()))
    return content


if __name__ == "__main__":
    app.run(host='localhost', port = 8080, debug=True)
