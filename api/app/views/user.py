from app import app
from flask_json import as_json, request, jsonify
from app.models.user import User
from flasgger import swag_from

@app.route("/users", methods=["GET"])
@swag_from('doc/user/list.yml')
def get_users():
    users = []
    query = User.select()
    for i in query:
        users.append(i.to_hash())
    return jsonify(users), 200

@app.route('/users', methods=['POST'])
@as_json
@swag_from('doc/user/post.yml')
def create_user():
    data = request.form
    email_check = User.select().where(User.email == data['email'])
    if email_check:
        return {'code': 10000, 'msg': 'Email already exists'}, 409

    user = User(
        email = data['email'],
        first_name = data['first_name'],
        last_name = data['last_name']
    )
    """Saving the hashed password"""
    user.set_password(data['password'])
    user.save()

    return {'code': 201,'msg': 'User was created successfully'}, 201

@app.route('/users/<int:id>', methods=['GET'])
@as_json
@swag_from('doc/user/get.yml')
def get_user(id):
    try:
        user = User.get(User.id == id)
    except Exception as e:
        return {'code': 404, 'msg': "User not found"}, 404

    return user.to_hash(), 200

@app.route('/users/<int:id>', methods=['PUT'])
@as_json
@swag_from('doc/user/put.yml')
def update_user(id):
    data = request.form
    user = User.get(User.id == id)
    for item in data:
        if item == 'email':
            raise Exception("Email can't be changed")
        if item == 'password':
            user.set_password(data['password'])
        else:
            setattr(user, item, data[item])

    user.save()
    return {'code': 200, 'msg': 'Updated successfully'}, 200

@app.route('/users/<int:id>', methods=['DELETE'])
@as_json
@swag_from('doc/user/delete.yml')
def del_user(id):
    id_check = User.select().where(User.id == id)
    if not id_check:
        return {'code': 404, 'msg': 'User not found'}, 404

    item = User.delete().where(User.id == id)
    item.execute()
    return {'code': 200, 'msg': 'Deleted successfully'}, 200
