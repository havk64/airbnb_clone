from peewee import ForeignKeyField, Model
from app.models.base import database
from app.models.place  import Place
from app.models.amenity import Amenity

class PlaceAmenities(Model):
    place = ForeignKeyField(Place)
    amenity = ForeignKeyField(Amenity)

    class Meta():
        database = database
