from datetime import datetime
import unittest, json, logging
from app.models.base import database
from app.models.user import User
from app import app

class UserTestCase(unittest.TestCase):
	def setUp(self):
		self.app = app.test_client()
		#logging.disable(logging.CRITICAL)
		database.create_tables([User], safe = True)

	def tearDown(self):
		database.drop_table(User)
	# Auxiliary function to return error message for assert function
	def errormsg(self, expec, *got):
		return 'Expecting {} but got {}'.format(expec, got)
	# Auxiliary function for creation of user
	def create_user(self, user, expec):
		resp = self.app.post('/users', data=user)
		assert resp.status == expec, self.errormsg(expec, resp.status)
		return User.select().order_by(User.id.desc()).get()

	def test_create(self):
		users = [
			{'first_name':'Alexandro','last_name':'de Oliveira',
                            'email':'alexandro.oliveira@holbertonschool.com',
                            'password':'123','is_admin':True},
			{'first_name':'Tony','last_name':'Stark',
                            'email':'tony@stark.com','password':'456',
                            'is_admin': False}]

		without_email = {'first_name': 'Jon', 'last_name': 'Snow',
                        'password': '321', 'is_admin': False}
		dupl_email = {'first_name': 'Cris','last_name': 'Lamarc',
                        'email': 'alexandro.oliveira@holbertonschool.com',
                        'password': '654', 'is_admin': True}

		count = 1
		for user in users:
			# It should create users with sequential ids.
			last_user = self.create_user(user, '201 CREATED')
			assert last_user.id == count, self.errormsg(count, last_user.id)
			count += 1
		# It should return bad request when email is not given.
		last_user = self.create_user(without_email, '400 BAD REQUEST')
		assert last_user.email == 'tony@stark.com',\
		self.errormsg('tony@stark.com', str(last_user.email)) # user not created
		# It should return 'CONFLICT' when using duplicated email.
		last_user = self.create_user(dupl_email, '409 CONFLICT')
		assert last_user.email == 'tony@stark.com',\
		self.errormsg('tony@stark.com', str(last_user.email))
