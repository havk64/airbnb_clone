from app.models.base import database
from app.models.user import User
from app.models.city import City
from app.models.state import State
from app.models.place import Place
from app.models.place_book import PlaceBook
from app.models.amenity import Amenity
from app.models.place_amenity import PlaceAmenities
from app.models.review import Review
from app.models.review_user import ReviewUser
from app.models.review_place import ReviewPlace

database.connect()
database.create_tables([User, State, City, Place, Amenity, PlaceBook, PlaceAmenities, Review, ReviewUser, ReviewPlace], safe = True)
database.close()
