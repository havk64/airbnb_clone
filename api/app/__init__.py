from flask import Flask
from flask_json import FlaskJSON

app = Flask(__name__)
app.config['JSON_ADD_STATUS'] = False

json = FlaskJSON(app)

from views import *
