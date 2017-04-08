import unittest, logging
from app.models.base import database
from app import app

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        logging.disable(logging.CRITICAL)
        database.create_tables([self.table], safe=True)

    def tearDown(self):
        database.drop_table(self.table)

    def errormsg(self, expec, *got):
        return 'Expecting {} but got {}'.format(expec, got)

    def check(self, value, expected):
        assert value == expected, self.errormsg(expected, value)

    def create_row(self, data, expec):
        resp = self.app.post(self.path, data=data)
        self.check(resp.status, expec)
        return self.table.select().order_by(self.table.id.desc()).get()
