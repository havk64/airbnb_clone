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
