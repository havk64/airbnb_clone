from peewee import CharField, ForeignKeyField
from base   import BaseModel
from state  import State

class City(BaseModel):
    """Definition of City Model"""
    name = CharField(128, null = False)
    state = ForeignKeyField(State, related_name='cities', on_delete='CASCADE')

    def to_hash(self):
        """Method to_hash returns City object model to hash"""
        state = State.get(State.id == self.state)
        city = {
            'name'      : self.name,
            'state_id'  : state.id,
        }
        return super(City, self).to_hash(self, city)
