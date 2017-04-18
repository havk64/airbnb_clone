from app.models.peewee import Model, ForeignKeyField
from app.models.base import database
from app.models.place import Place
from app.models.review import Review

class ReviewPlace(Model):
    place = ForeignKeyField(Place)
    review = ForeignKeyField(Review)

    class Meta:
        database = database
