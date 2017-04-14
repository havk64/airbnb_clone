from base import BaseTestCase
from app.models.amenity import Amenity
from app.models.place import Place
from fixtures import *
import unittest

class AmenitiesTestCase(BaseTestCase):
    table = [Amenity] # , User, State, City, Place, PlaceBook]
    path = '/amenities'
    example = fixt_amenities[0]

    def test_create(self):
        count = 1
        for amenity in fixt_amenities:
            last_amen = self.create_row(amenity, '201 CREATED')
            self.check(last_amen.id, count)
            count += 1
        # Bad request
        # duplicated

    def test_list(self):
        self.check_list()

    def test_get(self):
        self.check_get('Amenity')

    def test_delete(self):
        self.check_delete('Amenity')
