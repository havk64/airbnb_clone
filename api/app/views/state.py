from app import app
from app.models.state import State
from datetime import datetime
from flask_json import as_json, request, jsonify

@app.route('/states', methods = ['GET'])
def get_states():
    states = []
    query = State.select()
    for i in query:
        states.append(i.to_hash())
    return jsonify(states), 200

@app.route('/states', methods = ['POST'])
@as_json
def create_state():
    data = request.form
    name_check = State.select().where(State.name == data['name'])
    if name_check:
        return {'code': 10000, 'msg': 'State already exists'}, 409
    state = State.create(
        name = data['name']
    )
    return {'code': 201,'msg': 'State was created successfully'}, 201

@app.route('/states/<int:number>', methods = ['GET'])
@as_json
def get_state(number):
    try:
        state = State.get(State.id == number)
    except Exception as e:
        return {'code': 404, 'msg': "State not found"}, 404

    return state.to_hash(), 200

@app.route('/states/<int:number>', methods = ['DELETE'])
@as_json
def del_state(number):
    id_check = State.select().where(State.id == number)
    if not id_check:
        return {'code': 404, 'msg': 'User not found'}, 404

    item = State.delete().where(State.id == id)
    item.execute()
    return {'code': 200, 'msg': 'Deleted successfully'}, 200
