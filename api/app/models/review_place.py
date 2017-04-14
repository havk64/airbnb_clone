from peewee import Model, ForeignKeyField
from base import database
from place import Place
from review import Review

class ReviewPlace(Model):
    place = ForeignKeyField(Place)
    review = ForeignKeyField(Review)

    class Meta:
        database = database
