from peewee import Model, ForeignKeyField
from app.models.base import database
from app.models.user import User
from app.models.review import Review

class ReviewUser(Model):
    user = ForeignKeyField(User)
    review = ForeignKeyField(Review)

    class Meta:
        database = database
