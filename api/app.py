from app import app
from config import *
if __name__ == '__main__' :
    ''' Initializing the app'''
    app.run(host=HOST, port=PORT, debug=DEBUG)
