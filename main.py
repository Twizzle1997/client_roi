from config import ressources, db_access
from flask import Flask, jsonify
from config.db_access import DatabaseManager as db
import json
import requests
from bson.json_util import dumps

app = Flask(__name__)

@app.route("/")
def hello():
    return {"welcome_message": "World"}


@app.route("/api/request/<name>")
def route_default(name: str):

    response = requests.get(db.getInstance().get_country_by_name(name))
    content = json.loads(response.content.decode('utf-8'))

    if response.status_code != 200:
        return jsonify({
            'status': 'error',
            'message': 'La requête à l\'API n\'a pas fonctionné. Voici le message renvoyé par l\'API : {}'.format(content['message'])
        }), 500

    else :
        return content



if __name__ == "__main__":
    app.run(host='localhost', port = 8080, debug=True)
