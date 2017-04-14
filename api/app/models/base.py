from peewee import MySQLDatabase, PrimaryKeyField, Model, DateTimeField
from datetime import datetime
from config import *

database = MySQLDatabase(host       = DATABASE["host"],
                         port       = DATABASE["port"],
                         user       = DATABASE["user"],
                         password   = DATABASE["password"],
                         database   = DATABASE["database"])

class BaseModel(Model):
    id = PrimaryKeyField(unique=True)
    created_at = DateTimeField(default=datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    updated_at = DateTimeField(default=datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

    def save(self, *args, **kwargs):
        self.update_at = datetime.now()
        super(BaseModel, self).save()

    def to_hash(self, model, data):
        ''' Returns a hash of the BaseModel in the database '''
        data['id'] = self.id
        data['created_at'] = self.created_at
        data['updated_at'] = self.updated_at
        return data

    class Meta:
        database = database
        order_by = ("id", )
