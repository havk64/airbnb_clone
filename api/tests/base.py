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
	# Auxiliary function to return error message for assert function

    def errormsg(self, expec, *got):
        return 'Expecting {} but got {}'.format(expec, got)
