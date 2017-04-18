from app import app
from app.models.base import database
from flask_json import as_json
from datetime import datetime
from flasgger import swag_from


@app.route('/', methods=["GET"])
@as_json
@swag_from('doc/index/get.yml')
def index():
	utc = datetime.utcnow().strftime("%Y/%m/%d %H:%M:%S")
	now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
	return dict(status='OK', utc_time=utc, time=now)

def before_request():
	database.connect()

def after_request():
	database.close()

@app.errorhandler(404)
@as_json
@swag_from('doc/index/not_found.yml')
def not_found(error):
	return {'code': 404, 'msg':'not found'}, 404
