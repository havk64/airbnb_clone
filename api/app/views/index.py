from flask import Flask
from app import app
from app.models.base import database
from flask_json import FlaskJSON, as_json, jsonify
from datetime import datetime


@app.route('/', methods=["GET"])
@as_json
def index():
	utc = datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")
	now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
	return dict(status='OK', utc_time=utc, time=now)

def before_request():
	database.connect()

def after_request():
	database.close()

@app.errorhandler(404)
def not_found(error):
	return jsonify(code=404, msg='not found')#, 404
