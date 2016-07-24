from peewee import *
from base import *
from user import User
from city import City

class Place(BaseModel):
    """Definition of Place class"""
    owner = ForeignKeyField(User, related_name = "places")
    city = ForeignKeyField(City, related_name = "places")
    name = CharField(128, null = False)
    description = TextField()
    number_rooms = IntegerField(default = 0)
    number_bathrooms = IntegerField(default = 0)
    max_guest = IntegerField(default = 0)
    price_by_night = IntegerField(default = 0)
    latitude = FloatField()
    longitude = FloatField()
    def to_hash(self):
        """Method to return a hash of Place object model"""
        place = {
            'owner'         : User.get(User.id == self.owner),
            'owner_id'      : owner.id,
            'city'          : City.get(City.id == self.city),
            'city_id'       : city.id,
            'name'          : self.name,
            'description'   : self.description,
            'number_rooms'  : self.number_rooms,
            'number_bathrooms' : self.number_bathrooms,
            'max_guest'     : self.max_guest,
            'price_by_night': self.price_by_night,
            'latitute'      : self.latitute,
            'longitude'     : self.longitude
        }
        return super(Place, self).to_hash(self, place)
