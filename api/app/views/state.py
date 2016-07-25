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

@app.route('/states', methods = ['POST'])
@as_json
def create state():
    data = request.form
    name_check = State.select().where(State.name = data['name'])
    if name_check:
        return {'code': 10000, 'msg': 'State already exists'}, 409
    state = State.create(
        name = data['name']
    )
    return {'code': 201,'msg': 'State was created successfully'}, 201
