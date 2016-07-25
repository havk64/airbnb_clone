from app import app
from app.models.state import State
from datetime import datetime
from flask_json import as_json, request

@app.route('/states', methods = ['GET'])
def get_states():
    states = []
    query = State.select()
    for i in query:
        states.append(i.to_hash)
    return jsonify(states), 200
