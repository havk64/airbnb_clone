from app.models.city import City
from app.models.state import State
from app import app
from flask_json import as_json, request, jsonify

@app.route('/states/<int:id>/cities', methods=['GET'])
@as_json
def get_cities(id):
    cities = []
    #query = City.select(State.id == id)
    query = City.select().join(State).where(State.id == id)
    for i in query:
        cities.append(i.to_hash())
    #return {'msg':jsonify(cities)}, 200
    return jsonify(cities)

@app.route('/states/<int:id>/cities', methods=['POST'])
@as_json
def create_city(id):
    data = request.form
    city_check = City.select().join(State).where(State.id == id, City.name == data['name'])
    if city_check:
        return {'code': 10002, 'msg': 'City already exist in this state'},409

    city = City(
        name = data['name'],
        state = id
    )
    city.save()
    return {'code': 201, 'msg': 'City created successfully'}, 201

@app.route('/states/<int:sid>/cities/<int:id>', methods=['GET'])
@as_json
def get_city(sid, id):
    try:
        city = City.get(City.id == id, City.state == sid)
    except Exception:
        return {'code': 404, 'msg': 'City not found'}, 404

    return city.to_hash(), 200

@app.route('/states/<int:sid>/cities/<int:id>', methods=['DELETE'])
@as_json
def delete_city(sid, id):
    try:
        city = City.get(City.id == id, City.state == sid)
    except Exception:
        return {'code': 404, 'msg': 'City not found'}, 404

    city.delete_instance()
    return {'code': 200, 'msg': 'Deleted successfully'}, 200
