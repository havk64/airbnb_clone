import unittest, logging, json
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

    def check_dupl_entry(self, data, code):
        last_entry = self.create_row(data, '409 CONFLICT')
        resp = self.app.post(self.path, data=data)
        data = json.loads(resp.data)
        self.check(data['code'], code)
        return last_entry

    def check_list(self):
        # Get request to the table should return 0 when empty
        resp = self.app.get(self.path)
        data = json.loads(resp.data)
        self.check(len(data),0)
        # After item creation it should return the number of items
        self.create_row(self.example,'201 CREATED')
        resp = self.app.get(self.path)
        data = json.loads(resp.data)
        assert len(data) > 0, self.errormsg(1, len(data))
