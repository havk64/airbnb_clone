from base import BaseModel
from peewee import CharField

class Amenity(BaseModel):
    """Definition os Amenity Object Model"""
    name = CharField(128, null = False)

    def to_hash(self):
        """Method to_hash returns the Amenity Object model to hash"""
        amenity = {
            'name'  = self.name,
        }
        return super(Amenity, self).to_hash(self, amenity)
