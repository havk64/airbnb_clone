from peewee import *
from base   import BaseModel
from place  import Place
from user   import User

class PlaceBook(BaseModel):
    place = ForeignKeyField(Place)
    user = ForeignKeyField(User, related_name = "places_booked")
    is_validated = BooleanField(default = False)
    date_start = DateTimeField(null = False)
    number_nights = IntegerField(default = 1)
