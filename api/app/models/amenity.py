from base import BaseModel
from peewee import CharField

class Amenity(BaseModel):
    name = CharField(128, null = False)

    def to_hash(self):
        amenity = {
            'name'  = self.name,
        }
        return super(Amenity, self).to_hash(self, amenity)
