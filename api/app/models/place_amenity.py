from peewee import ForeignKeyField, Model
from base import database
from place  import Place
from amenity import Amenity

class PlaceAmenities(Model):
    place = ForeignKeyField(Place)
    amenity = ForeignKeyField(Amenity)

    class Meta():
        database = database
