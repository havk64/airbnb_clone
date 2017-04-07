from peewee import CharField
from app.models.base import BaseModel

class State(BaseModel):
    """State model definition"""
    name = CharField(128, null = False, unique = True)

    def to_hash():
        """Method to return the hash of State object model"""
        state = {
				'name': self.name
        }
        return super(State, self).to_hash(self, state)
