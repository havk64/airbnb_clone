from base import BaseTestCase
from app.models.state import State
import json

class StateTestCase(BaseTestCase):
	table = State
	path = '/states'
	states = [
			{'name': 'California'}, {'name': 'New York'}, {'name': 'Florida'},
			{'name':  'Massachusetts'}, {'name': 'Hawaii'}, {'name': 'District of Columbia'}
		]

	example = states[0]

	def test_create(self):
		# It should create states with sequential ids.
		count = 1
		for state in self.states:
			last_state = self.create_row(state, '201 CREATED')
			assert last_state.id == count, self.errormsg(count, last_state.id)
			assert last_state.name == state['name'], self.errormsg(state['name'], last_state.id)
			count += 1
		# It should return code 10001 when trying to create duplicated state name.
		dupl_state = {'name': 'California'}
		last_state = self.check_dupl_entry(dupl_state, 10001)
		# The last entry on database should be the previous one
		assert last_state.name == 'District of Columbia', self.errormsg('District of Columbia',last_state.name)


	def test_list(self):
		self.check_list()

	def test_get(self):
		self.check_get('State')

	def test_delete(self):
		# It should create state
		last_state = self.create_row(self.states[0], '201 CREATED')
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
