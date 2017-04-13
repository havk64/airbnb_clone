from base import BaseTestCase
from app.models.user import User
from fixtures import *

class UserTestCase(BaseTestCase):
	table = [User]
	path = '/users'
	example = fixt_users[0]

	def test_create(self):
		count = 1
		for user in fixt_users:
			# It should create users with sequential ids.
			last_user = self.create_row(user, '201 CREATED')
			self.check(last_user.id, count)
			count += 1
		# It should return bad request when email is not given.
		last_user = self.create_row(fixt_bad_req, '400 BAD REQUEST')
		self.check(last_user.email, 'jon@snow.com') # user not created
		# It should return code 10001 when trying to create user with duplicated email
		last_user = self.check_dupl_entry(fixt_dupl_email, 10000)
		self.check(last_user.email, 'jon@snow.com')

	def test_list(self):
		self.check_list()

	def test_get(self):
		self.check_get('User')

	def test_delete(self):
		self.check_delete('User')

	def test_update(self):
		upd_data = {'first_name':'George', 'last_name':'Harrison'}
		self.check_update(upd_data)
		# It should raise an error when trying to change email
		with self.assertRaises(Exception) as context:
			resp = self.app.put('{}/{}'.format(self.path, 1), data={'email':'new@email.com'})
		self.assertTrue('Email can\'t be changed' in str(context.exception))
