from app import app
from app.models.place_book import PlaceBook
from app.models.place import Place
from flask_json import as_json, request, jsonify
from datetime import datetime

@app.route('/places/<int:id>/books', methods=['GET'])
@as_json
def get_books(id):
    books = []
    query = PlaceBook.select().join(Place).where(Place.id == id)
    for book in query:
        books.append(book.to_hash())
    return jsonify(books)

@app.route('/places/<int:id>/books', methods=['POST'])
@as_json
def create_books(id):
    data = request.form
    book = PlaceBook()
    book.place = id
    for entry in data:
        if entry == 'date_start':
            setattr(book, entry, datetime.strptime(data[entry], '%Y/%m/%d %H:%M:%S'))
        else:
            setattr(book, entry, data[entry])

    book.save()
    return {'code': 201, 'msg': 'Book created successfully'}, 201

@app.route('/places/<int:pid>/books/<int:id>', methods=['GET'])
@as_json
def get_book(pid, id):
    try:
        book = PlaceBook.get(PlaceBook.id == id, PlaceBook.place_id == pid)
    except Exception:
        return {'code': 404, 'msg': 'Book not found'}, 404

    return book.to_hash(), 200

@app.route('/places/<int:pid>/books/<int:id>', methods=['DELETE'])
@as_json
def delete_book(pid, id):
    try:
        book = PlaceBook.get(PlaceBook.id == id, PlaceBook.place_id == pid)
    except Exception:
        return {'code': 404, 'msg': 'Book not found'}, 404

    book.delete_instance()
    return {'code':200, 'msg': 'Deleted successfully'}, 200

@app.route('/places/<int:pid>/books/<int:id>', methods=['PUT'])
@as_json
def update_books(pid, id):
    data = request.form
    try:
        book = PlaceBook.get(PlaceBook.id == id, PlaceBook.place_id == pid)
    except Exception:
        return {'code': 404, 'msg': 'Book not found'}, 404

    for i in data:
        if i == 'user':
            raise Exception("User can't be changed")
        if i == 'place':
            setattr(book, 'place_id', data[i])
        elif i == 'date_start':
            setattr(book, i, datetime.strptime(data[i], '%Y/%m/%d %H:%M:%S'))
        else:
            setattr(book, i, data[i])

    book.save()
    return {'code': 200, 'msg': 'Updated successfully'}, 200
