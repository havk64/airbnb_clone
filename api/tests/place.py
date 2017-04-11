from base import BaseTestCase
from app.models.place import Place
from app.models.state import State
from app.models.city import City
from app.models.user import User
from fixtures import *
import unittest

class PlaceTestCase(BaseTestCase):
    table = [User, State, City, Place]
    path = '/places'
    example = fixt_places[0]

    def create_states_and_cities(self):
        state_table = {'model': State, 'path':'/states'}
        city_table = {'model': City, 'path': '/states/1/cities'}
        for state in fixt_states:
            last_state = self.create(state_table, state)
        for city in fixt_cities:
            last_city = self.create(city_table, city)
        return (last_state, last_city)

    def test_cities(self):
        last_state, last_city = self.create_states_and_cities()
        self.check(last_state.name, fixt_states[-1]['name'])
        self.check(last_city.name, fixt_cities[-1]['name'])
        city = City.get(City.id == 3, City.state == 1)
        self.check(fixt_cities[2]['name'], city.name)

    def create_users(self):
        user_table = {'model': User, 'path':'/users'}
        for user in fixt_users:
            last_user = self.create(user_table, user)
        return last_user

    def test_users(self):
        last_user = self.create_users()
        self.check(last_user.email, fixt_users[-1]['email'])

    def test_create(self):
        self.create_states_and_cities()
        self.create_users()
        count = 1
        for place in fixt_places:
            # It should create a place with sequential ids.
            last_place = self.create_row(place, '201 CREATED')
            self.check(last_place.id, count)
            count += 1

	    # It should return bad request with bad data.
        last_place = self.create_row(fixt_place_br, '400 BAD REQUEST')
        self.check(last_place.id, 3)
        # It should return code 10003 when trying to create place with duplicated name
        #last_place = self.create_row(fixt_dupl_place, 10003)
        #self.check(last_place.id, 3)

    def test_list(self):
        self.create_states_and_cities()
        self.create_users()
        self.check_list()

    def test_get(self):
        self.create_states_and_cities()
        self.create_users()
        self.check_get('Place')

    def test_delete(self):
        self.create_states_and_cities()
        self.create_users()
        self.check_delete('Place')

    def test_update(self):
        self.create_states_and_cities()
        self.create_users()
        upd_data = {'name':'Hilton', 'number_bathrooms':2, 'max_guest': 10}
        self.check_update(upd_data)
