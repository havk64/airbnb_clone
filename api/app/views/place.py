from app.models.place import Place
from app.models.city import City
from app.models.state import State
from app import app
from flask_json import as_json, request, jsonify

@app.route('/places', methods=['GET'])
@as_json
def get_places():
    places = []
    query = Place.select()
    for i in query:
        places.append(i.to_hash())
    return jsonify(places)

@app.route('/places', methods=['POST'])
@as_json
def create_places():
    data = request.form
    #place_check = Place.get(Place.owner == data['owner'],
    #                        Place.name == data['name'],
    #                        Place.city == data['city]'])
    #if place_check:
    #    return {'code': 10003, 'msg': 'Place already exists'}, 409

    place = Place.create(
        owner = data['owner'],
        city = data['city'],
        name = data['name'],
        description = data['description'],
        number_rooms = data['number_rooms'],
        number_bathrooms = data['number_bathrooms'],
        max_guest = data['max_guest'],
        price_by_night = data['price_by_night'],
        latitude = data['latitude'],
        longitude = data['longitude']
    )
    return {'code': 201,'msg': 'Place created successfully'}, 201

@app.route('/places/<int:id>', methods=['GET'])
@as_json
def get_place(id):
    try:
        place = Place.get(Place.id == id)
    except Exception:
        return {'code': 404, 'msg': 'Place not found'}, 404

    return place.to_hash(), 200

@app.route('/places/<int:id>', methods=['PUT'])
@as_json
def update_place(id):
    data = request.form
    try:
        place = Place.get(Place.id == id)
    except Exception:
        return {'code': 404, 'msg': 'Place not found'}, 404

    for i in data:
        switch = {
            'owner'             : 'owner_id',
            'city'              : 'city_id',
            'name'              : 'name',
            'description'       : 'description',
            'number_rooms'      : 'number_rooms',
            'number_bathrooms'  : 'number_bathrooms',
            'max_guest'         : 'max_guest',
            'price_by_night'    : 'price_by_night',
            'latitude'          : 'latitude',
            'longitude'         : 'longitude'
        }.get(i)
        setattr(place, switch, data[i])

    place.save()
    return {'code': 200, 'msg': 'Updated successfully'}, 200

@app.route('/places/<int:id>', methods=['DELETE'])
@as_json
def delete_place(id):
    try:
        place = Place.get(Place.id == id)
    except Exception:
        return {'code': 404, 'msg': 'Place not found'}, 404

    place.delete_instance()
    return {'code': 200, 'msg': 'Deleted successfully'}, 200
