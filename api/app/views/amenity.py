from app import app
from app.models.amenity import Amenity
from app.models.place import Place
from flask_json import request, as_json, jsonify

@app.route('/amenities', methods=['GET'])
@as_json
def get_amenities():
    amenities = []
    query = Amenity.select()
    for i in query:
        amenities.append(i.to_hash())

    return jsonify(amenities)

@app.route('/amenities', methods=['POST'])
@as_json
def create_amenities():
    data = request.form
    check_amenity =  Amenity.select(). where(Amenity.name == data['name'])
    if check_amenity:
        return {'code': 10003, 'msg': 'Name already exists'}, 409

    amenity = Amenity.create(
        name = data['name']
    )
    return {'code': 201, 'msg': 'Amenity created successfully'}, 201

@app.route('/amenities/<int:id>', methods=['GET'])
@as_json
def get_amenity(id):
    try:
        amenity = Amenity.get(Amenity.id == id)
    except Exception:
        return {'code': 404, 'msg': 'Amenity not found'}, 404

    return amenity.to_hash(), 200

@app.route('/amenities/<int:id>', methods=['DELETE'])
@as_json
def delete_amenity(id):
    try:
        amenity = Amenity.get(Amenity.id == id)
    except Exception:
        return {'code': 404, 'msg': 'Amenity not found'}, 404

    amenity.delete_instance()
    return {'code': 200, 'msg': 'Deleted successfully'}, 200

@app.route('/places/<int:id>/amenities', methods=['GET'])
@as_json
def get_amenity_by_place(id):
    amenities = []
    query = Amenity.select().where(Place.id == id)
    for i in query:
        amenities.append(i.to_hash())

    return jsonify(amenities)
