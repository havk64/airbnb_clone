from peewee import TextField, IntegerField, ForeignKeyField
from app.models.base import BaseModel
from app.models.user import User
from app.models.review_user import ReviewUser
from app.models.review_place import ReviewPlace

class Review(BaseModel):
    message = TextField(null=False)
    stars = IntegerField(default=0)
    user = ForeignKeyField(User, related_name='reviews', on_delete='CASCADE')

    def to_hash(self):
        user = User.get(User.id == self.user)
        review = {
            'from_user_id'  : user.id,
            'to_user_id'    : ReviewUser,
            'to_place_id'   : ReviewPlace,
            'stars'          : self.stars,
            'message'       : self.message
            }
        return super(Review, self).to_hash(self, review)
