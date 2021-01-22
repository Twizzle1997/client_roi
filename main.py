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

# @app.route("/api/request/<name>")
# def route_default(name: str):

#     response = requests.get(db.getInstance())

#     if response.status_code != 200:
#         return jsonify({
#             'status': 'error',
#             'message': 'La requête à l\'API n\'a pas fonctionné.'
#         }), 500

#     else :
#         content = json.loads(dumps(db.getInstance().get_country_by_name(name)))
#         return content


if __name__ == "__main__":
    app.run(host='localhost', port = 8080, debug=True)
