from app import app
from datetime import datetime
import unittest, json, logging
from app.models.base import database
from app.models.user import User

class UserTestCase(unittest.TestCase):
	def setUp(self):
		self.app = app.test_client()
		#logging.disable(logging.CRITICAL)
		database.create_tables([User], safe = True)

	def tearDown(self):
		database.drop_table(User)

	def errormsg(self, expec, *got):
		return 'Expecting {} but got {}'.format(expec, got)

	def test_create(self):
		users = [
			{'first_name': 'Alexandro','last_name': 'de Oliveira', 'email': 'alexandro.oliveira@holbertonschool.com','password': '123', 'is_admin': True},
			{'first_name': 'Tony', 'last_name': 'Stark', 'email': 'tony@stark.com', 'password':'456', 'is_admin': False}
		]

		without_email = {'first_name': 'Jon', 'last_name': 'Snow', 'password': '321', 'is_admin': False}
		dupl_email = {'first_name': 'Cris','last_name': 'Lamarc', 'email': 'alexandro.oliveira@holbertonschool.com','password': '654', 'is_admin': True}

		count = 1
		for user in users:
			resp = self.app.post('/users', data=user)
			assert resp.status_code == 201, self.errormsg(201, resp.status_code)
			assert resp.status == '201 CREATED', self.errormsg('201 CREATED', resp.status)
			last_user = User.select().order_by(User.id.desc()).get()
			assert last_user.id == count, self.errormsg(count, last_user.id)
			count += 1

		resp = self.app.post('/users', data=without_email)
		assert resp.status == '400 BAD REQUEST', self.errormsg('400 BAD REQUEST', resp.status)
		last_user = User.select().order_by(User.id.desc()).get()
		assert last_user.email == 'tony@stark.com', self.errormsg('tony@stark.com', str(last_user.email))

		resp = self.app.post('/users', data=dupl_email)
		assert resp.status == '409 CONFLICT', self.errormsg('409 CONFLICT', resp.status)
		last_user = User.select().order_by(User.id.desc()).get()
		assert last_user.email == 'tony@stark.com', self.errormsg('tony@stark.com', str(last_user.email))
