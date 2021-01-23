from config import ressources, db_access
from flask import Flask, jsonify
from config.db_access import DatabaseManager as db
import json
from bson.json_util import dumps
from config.ressources import *
from flask import request
import ast

app = Flask(__name__)

@app.route("/")
def hello():
    return {"welcome_message": "World"}


# VISUALISATION D'UN PAYS.
@app.route("/api/request/<name>", methods=['GET'])
def route_request(name: str):

    content = json.loads(dumps(db.getInstance().get_country_by_name(name)))
    return content

# AJOUT D'UN PAYS FICTIF.
@app.route("/api/add", methods=['POST'])
def  route_add():
    
    name=(request.get_data().decode().split('=')[1])
    content = json.loads(dumps(db.getInstance().set_country(name)))

    return content

# SUPPRESSION D'UN PAYS.
@app.route("/api/remove", methods=['DELETE'])
def  route_remove():

    name=request.get_data().decode().split('=')[1]
    content = json.loads(dumps(db.getInstance().delete_country_by_name(name)))
    return content

# MISE A JOUR D'UN PAYS.
@app.route("/api/update", methods=["PUT"])
def  route_edit():

    name=request.form.get("name")
    couple=ast.literal_eval(request.form.get("couple"))

    content = json.loads(dumps(db.getInstance().update_country_by_name(name, couple)))

    return content

# CLASSIFICATION DES PAYS.
@app.route("/api/class", methods=["GET"])
def  route_categorize():

    content = json.loads(dumps(db.getInstance().get_countries_class()))
    return content


if __name__ == "__main__":
    app.run(host='localhost', port = 8080, debug=True)
