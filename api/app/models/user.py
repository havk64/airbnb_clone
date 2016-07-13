from peewee import CharField, BooleanField
from base import BaseModel
from hashlib import md5

class User(BaseModel):
    email = CharField(128, null = False, unique = True)
    password = CharField(128, null = False)
    first_name = CharField(128, null = False)
    last_name = CharField(128, null = False)
    is_admin = BooleanField(default = False)

    def set_password(self, clear_password):
        self__.password = md5(clear_password).hexdigest()
