from base import BaseTestCase
from app.models.place_book import PlaceBook
from app.models.user import User
from app.models.place import Place
from app.models.state import State
from app.models.city import City
from fixtures import *

class PlaceBookTestCase(BaseTestCase):
    table = [User, State, City, Place, PlaceBook]
    path = '/places/1/books'
    example = fixt_pbooks[0]

    def create_places_users(self):
        self.create_states_and_cities()
        place_table = {'model': Place, 'path': '/places'}
        user_table = {'model': User, 'path': '/users'}
        for user in fixt_users:
            last_user= self.create(user_table, user)
            self.check(last_user.email, user['email'])
        for place in fixt_places:
            last_place = self.create(place_table, place)
            self.check(last_place.name, place['name'])

    def test_create(self):
        self.create_places_users()
        count = 1
        for pb in fixt_pbooks:
            last_pbook = self.create_row(pb, '201 CREATED')
            self.check(last_pbook.id, count)
            count += 1
        # bad request
        # duplicated

    def test_list(self):
        self.create_places_users()
        self.check_list()

    def test_get(self):
        self.create_places_users()
        self.check_get('Book')

    def test_update(self):
        self.create_places_users()
        upd_data = {'date_start': '2016/07/20 09:01:10', 'is_validated': True, 'number_nights': 10}
        self.check_update(upd_data)

        # It should raise an error when trying to change user
        with self.assertRaises(Exception) as context:
            resp = self.app.put('{}/{}'.format(self.path, 1), data={'user': 2})
        self.assertTrue('User can\'t be changed' in str(context.exception))

    def test_delete(self):
        self.create_places_users()
        self.check_delete('Book')
