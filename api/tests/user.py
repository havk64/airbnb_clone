from base import BaseTestCase
from app.models.user import User
from data import *
import json

class UserTestCase(BaseTestCase):
	table = [User]
	path = '/users'
	example = users[0]

	def test_create(self):
		count = 1
		for user in users:
			# It should create users with sequential ids.
			last_user = self.create_row(user, '201 CREATED')
			self.check(last_user.id, count)
			count += 1
		# It should return bad request when email is not given.
		last_user = self.create_row(without_email, '400 BAD REQUEST')
		assert last_user.email == 'jon@snow.com',\
		self.errormsg('jon@snow.com', str(last_user.email)) # user not created
		# It should return code 10001 when trying to create user with duplicated email
		last_user = self.check_dupl_entry(dupl_email, 10000)
		assert last_user.email == 'jon@snow.com',\
		self.errormsg('jon@snow.com', str(last_user.email))
		# It should return code 10000 when user's email is duplicated

	def test_list(self):
		self.check_list()

	def test_get(self):
		self.check_get('User')
        # assert last_user.email == self.users[0]['email'], self.errormsg(self.users['email'], last_user.email)

	def test_delete(self):
		self.check_delete('User')

	def test_update(self):
		upd_data = {'first_name':'George', 'last_name':'Harrison'}
		self.check_update(upd_data)

		# It should give internal server error when trying to change email
		resp = self.app.put('{}/{}'.format(self.path, 1), data={'email':'new@email.com'})
		self.check(resp.status_code, 500)
