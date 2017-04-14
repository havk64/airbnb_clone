from peewee import Model, ForeignKeyField
from base import database
from user import User
from review import Review

class ReviewUser(Model):
    user = ForeignKeyField(User)
    review = ForeignKeyField(Review)

    class Meta:
        database = database
