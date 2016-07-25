from app.models.place import Place
from app.models.city import City
from app.models.state import State
from app import app
from flask import Flask, request, jsonify
from flask_json import FlaskJSON, as_json
from index import before_request, after_request

@app.route("/places", methods=["GET"])
def get_places():
    places = []
    query = Place.select()
    for i in query:
        places.append(i.to_hash())
    return jsonify(places), 200
