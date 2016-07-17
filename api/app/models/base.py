from peewee import *
from config import *
from datetime import datetime

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

    def to_hash(model, self, data):
        ''' Returns a hash of the BaseModel in the database '''
        data['id'] = self.id
        data['created_at'] = self.created_at.strftime("%d/%m/%Y %H:%M:%S")
        data['updated_at'] = self.updated_at.strftime("%d/%m/%Y %H:%M:%S")
        return data

    class Meta:
        database = database
        order_by = ("id", )
