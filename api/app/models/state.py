from peewee import CharField
from base import BaseModel

class State(BaseModel):
    name = CharField(128, null = False, unique = True)
    def to_hash():
        place = {
				'name': self.name
        }
        return super(State, self).to_hash(self, place)
