from peewee import CharField, BooleanField
from base import *
from hashlib import md5

class User(BaseModel):
    email = CharField(128, null = False, unique = True)
    password = CharField(128, null = False)
    first_name = CharField(128, null = False)
    last_name = CharField(128, null = False)
    is_admin = BooleanField(default = False)

    def set_password(self, clear_password):
        self.password = md5(clear_password).hexdigest()

    def to_hash(self):
        user = {
			'email': self.email,
			'first_name': self.first_name,
			'last_name': self.last_name,
			'is_admin': self.is_admin
            }
        return super(User, self).to_hash(self, user)
