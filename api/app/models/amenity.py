from base import BaseModel
from peewee import CharField

class Amenity(BaseModel):
    name = CharField(128, null = False)
