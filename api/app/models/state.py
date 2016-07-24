from peewee import CharField
from base import BaseModel

class State(BaseModel):
    """State class definition"""
    name = CharField(128, null = False, unique = True)

    def to_hash():
        """Function to return the hash of State object model"""
        place = {
				'name': self.name
        }
        return super(State, self).to_hash(self, place)
