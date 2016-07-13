from flask import Flask
from app.views import *
from app import app
from config import HOST, PORT, DEBUG

app.run(host=HOST, port=PORT, debug=DEBUG)
