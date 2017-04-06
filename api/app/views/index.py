from app import app
from app.models.base import database
from flask_json import as_json
from datetime import datetime


@app.route('/', methods=["GET"])
@as_json
def index():
	"""Output for requests to the root dir"""
	utc = datetime.utcnow().strftime("%Y/%m/%d %H:%M:%S")
	now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
	return dict(status='OK', utc_time=utc, time=now)

def before_request():
	database.connect()

def after_request():
	database.close()

@app.errorhandler(404)
@as_json
def not_found(error):
	"""Response for not found"""
	return {'code': 404, 'msg':'not found'}, 404
