from base import BaseTestCase
from app.models.city import City
from app.models.state import State
from fixtures import fixt_states, fixt_cities

class CityTestCase(BaseTestCase):
    table = [State, City]
    path = '/states/1/cities'
    example = fixt_cities[0]

    def create_states(self):
        state_table = {'model': State, 'path':'/states'}
        for state in fixt_states:
            last_state = self.create(state_table, state)

    def test_create(self):
        self.create_states()
        count = 1

        for city in fixt_cities:
        # It should create users with sequential ids.
            last_city = self.create_row(city, '201 CREATED')
            self.check(last_city.id, count)
            count += 1

        # It should return code 10002 when trying to create city with duplicated namne
        last_city = self.check_dupl_entry({'name':'San Francisco'}, 10002)
        self.check(last_city.name, 'Berkeley')

    def test_list(self):
        self.create_states()
        self.check_list()

    def test_get(self):
        self.create_states()
        self.check_get('City')

    def test_delete(self):
        self.create_states()
        self.check_delete('City')
