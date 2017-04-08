from base import BaseTestCase
from app.models.user import User
import json

class UserTestCase(BaseTestCase):
	table = User
	path = '/users'
	users = [
			{'first_name':'Alexandro','last_name':'de Oliveira',
                            'email':'alexandro.oliveira@holbertonschool.com',
                            'password':'123','is_admin':True},
			{'first_name':'Tony','last_name':'Stark',
                            'email':'tony@stark.com','password':'456',
                            'is_admin': False},
			{'first_name':'Jon', 'last_name':'Snow',
							'email':'jon@snow.com', 'password':'789'}]

	def test_create(self):
		without_email = {'first_name': 'Jon', 'last_name': 'Snow',
                        'password': '321', 'is_admin': False}
		dupl_email = {'first_name': 'Cris','last_name': 'Lamarc',
                        'email': 'alexandro.oliveira@holbertonschool.com',
                        'password': '654', 'is_admin': True}

		count = 1
		for user in self.users:
			# It should create users with sequential ids.
			last_user = self.create_row(user, '201 CREATED')
			self.check(last_user.id, count)
			count += 1
		# It should return bad request when email is not given.
		last_user = self.create_row(without_email, '400 BAD REQUEST')
		assert last_user.email == 'jon@snow.com',\
		self.errormsg('jon@snow.com', str(last_user.email)) # user not created
		# It should return 'CONFLICT' when using duplicated email.
		last_user = self.create_row(dupl_email, '409 CONFLICT')
		assert last_user.email == 'jon@snow.com',\
		self.errormsg('jon@snow.com', str(last_user.email))
		# It should return code 10000 when user's email is duplicated
		resp = self.app.post('/users', data=dupl_email)
		data = json.loads(resp.data)
		assert data['code'] == 10000, self.errormsg(10000, data['code'])

	def test_list(self):
		# Get request to 'users' should return 0 when empty
		resp = self.app.get('/users')
		data = json.loads(resp.data)
		assert len(data) == 0, self.errormsg(0, data)
		# After user creation it should return the number of items
		self.create_row(self.users[0],'201 CREATED')
		resp = self.app.get('/users')
		data = json.loads(resp.data)
		assert len(data) > 0, self.errormsg(1, len(data))

	def test_get(self):
		# Check the status code after create user(the assert is inside the function create user)
		last_user = self.create_row(self.users[0], '201 CREATED')
		resp = self.app.get('/users/{}'.format(last_user.id))
		# Check that is the same resource as the creation
		assert last_user.email == self.users[0]['email'], self.errormsg(self.users['email'], last_user.email)
		data = json.loads(resp.data)
		assert data['id'] == last_user.id, self.errormsg(last_user.id, data['id'])
		# Check when the user doesn't exist
		resp = self.app.get('/users/42')
		data = json.loads(resp.data)
		assert resp.status_code == 404, self.errormsg(404, resp.status_code)
		assert data['msg'] == 'User not found', self.errormsg('User not found', data['msg'])
		assert data['code'] == 404, self.errormsg(404, data['code'])

	def test_delete(self):
		# It should create user
		last_user = self.create_row(self.users[0], '201 CREATED')
		resp = self.app.get('/users/{}'.format(last_user.id))
		assert last_user.email == self.users[0]['email'], self.errormsg(self.users[0]['email'], last_user.email)
		# It should delete the user by its ID
		resp = self.app.delete('/users/{}'.format(last_user.id))
		data = json.loads(resp.data)
		assert data['msg'] == 'Deleted successfully', self.errormsg('',data['msg'])
		# It should return 404 for the delete user
		resp = self.app.get('/users/{}'.format(last_user.id))
		assert resp.status_code == 404, self.errormsg(404, resp.status_code)
		# It should not be possible to delete user not in database
		resp = self.app.delete('/users/42')
		assert resp.status_code == 404, self.errormsg(404, resp.status_code)
		data = json.loads(resp.data)
		assert data['msg'] == 'User not found', self.errormsg('User not found', data['msg'])

	def test_update(self):
		# It should create a user and it should be equal to specified user
		user = self.users[0]
		last_user = self.create_row(user, '201 CREATED')
		assert last_user.email == user['email'], self.errormsg(user['email'], last_user.email)
		# It should return update message when updated
		resp = self.app.put('/users/{}'.format(last_user.id), data={'first_name':'George', 'last_name':'Harrison'})
		upd_stat = json.loads(resp.data)
		assert upd_stat['msg'] == 'Updated successfully', self.errormsg('Updated successfully', upd_stat['msg'])
		# It should match the updated user with the update request
		resp = self.app.get('users/{}'.format(last_user.id))
		upd_user = json.loads(resp.data)
		assert upd_user['first_name'] == 'George', self.errormsg('George',last_user.first_name)
		# It should give internal server error when trying to change email
		resp = self.app.put('/users/{}'.format(last_user.id), data={'email':'new@email.com'})
		assert resp.status_code == 500, self.errormsg(500,resp.status_code)
