import unittest, json, logging
from app.models.base import database
from app.models.state import State
from app import app

class StateTestCase(unittest.TestCase):
	def setUp(self):
		self.app = app.test_client()
		logging.disable(logging.CRITICAL)
		database.create_tables([State], safe = True)
		self.states = [
			{'name': 'California'}, {'name': 'New York'}, {'name': 'Florida'},
			{'name':  'Massachusetts'}, {'name': 'Hawaii'}, {'name': 'District of Columbia'}
		]

	def tearDown(self):
		database.drop_table(State)

	def errormsg(self, expec, *got):
		return 'Expecting {} but got {}'.format(expec, got)

	def create_state(self, state, expec):
		resp = self.app.post('/states', data=state)
		assert resp.status == expec, self.errormsg(expec, resp.status)
		return State.select().order_by(State.id.desc()).get()

	def test_create(self):
		# It should create states with sequential ids.
		count = 1
		for state in self.states:
			last_state = self.create_state(state, '201 CREATED')
			assert last_state.id == count, self.errormsg(count, last_state.id)
			assert last_state.name == state['name'], self.errormsg(state['name'], last_state.id)
			count += 1
		# It should return 'CONFLICT' when using duplicated state name.
		dupl_state = 'California'
		last_state = self.create_state({'name': dupl_state}, '409 CONFLICT')
		# The last entry on database should be the previous one
		assert last_state.name == 'District of Columbia', self.errormsg('District of Columbia',last_state.name)
		# It should return code 10001 when state is duplicated
		resp = self.app.post('/states', data={'name': dupl_state})
		data = json.loads(resp.data)
		assert data['code'] == 10001, self.errormsg(10001, data['code'])

	def test_list(self):
		# When empty it should return 0 to the Get request
		resp = self.app.get('/states')
		data = json.loads(resp.data)
		assert len(data) == 0, self.errormsg(0, data)
		# After creation of state it should return the amont of items
		last_state = self.create_state(self.states[0], '201 CREATED')
		resp = self.app.get('/states')
		data = json.loads(resp.data)
		assert len(data) > 0, self.errormsg(1, len(data))

	def test_get(self):
		last_state = self.create_state(self.states[0], '201 CREATED')
		resp = self.app.get('/states/{}'.format(last_state.id))
		# Check that is the same resource as the creation
		assert last_state.name == self.states[0]['name'], self.errormsg(self.users['name'], last_state.name)
		data = json.loads(resp.data)
		assert data['id'] == last_state.id, self.errormsg(last_state.id, data['id'])
		# Check when the user doesn't exist
		resp = self.app.get('/states/42')
		data = json.loads(resp.data)
		assert resp.status_code == 404, self.errormsg(404, resp.status_code)
		assert data['msg'] == 'State not found', self.errormsg('State not found', data['msg'])
		assert data['code'] == 404, self.errormsg(404, data['code'])

	def test_delete(self):
		# It should create state
		last_state = self.create_state(self.states[0], '201 CREATED')
		resp = self.app.get('/states/{}'.format(last_state.id))
		assert last_state.name == self.states[0]['name'], self.errormsg(self.states[0]['name'], last_state.name)
		# It should delete the state by its ID
		resp = self.app.delete('/states/{}'.format(last_state.id))
		data = json.loads(resp.data)
		assert data['msg'] == 'Deleted successfully', self.errormsg('',data['msg'])
		# It should return 404 for the delete state
		resp = self.app.get('/states/{}'.format(last_state.id))
		assert resp.status_code == 404, self.errormsg(404, resp.status_code)
		# It should not be possible to delete state not in database
		resp = self.app.delete('/states/42')
		assert resp.status_code == 404, self.errormsg(404, resp.status_code)
		data = json.loads(resp.data)
		assert data['msg'] == 'State not found', self.errormsg('State not found', data['msg'])
