from peewee import CharField, ForeignKeyField
from base   import BaseModel
from state  import State

class City(BaseModel):
    name = CharField(128, null = False)
    state = ForeignKeyField(State, related_name='cities', on_delete='CASCADE')
    def to_hash():
        city = {
            'name'      : self.name,
            'state_id'  : state.id,
        }
        return super(City, self).to_hash(self, city)
