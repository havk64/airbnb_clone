from peewee import CharField, ForeignKeyField
from base   import BaseModel
from state  import State

class City(BaseModel):
    name = CharField(128, null = False)
    state = ForeignKeyField(State, related_name='cities', on_delete='CASCADE')
