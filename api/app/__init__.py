from flask import Flask
from flask_json import FlaskJSON
from flasgger import Swagger

app = Flask(__name__)
app.config['JSON_ADD_STATUS'] = False
app.config.update(
    PROPAGATE_EXCEPTIONS = True
)
Swagger(app)

json = FlaskJSON(app)

from app.views import *
