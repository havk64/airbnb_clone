from peewee import *
from base   import BaseModel
from place  import Place
from user   import User

class PlaceBook(BaseModel):
    """Definition of PlacBook Model"""
    place = ForeignKeyField(Place)
    user = ForeignKeyField(User, related_name = "places_booked")
    is_validated = BooleanField(default = False)
    date_start = DateTimeField(null = False)
    number_nights = IntegerField(default = 1)

    def to_hash(self):
        """Method to_hash returns the Placebook object model"""
        user = User.get(User.id == self.user)
        place = Place.get(Place.id == self.place)
        placebook = {
            'place_id'      = place.id,
            'user_id'       = user.id,
            'is_validated'  = self.is_validated,
            'date_start'    = self.date_start.strftime("%Y/%m/%d %H:%M:%S"),
            'number_nights' = self.number_nights
        }
        return super(PlaceBook, self).to_hash(self, placebook)
