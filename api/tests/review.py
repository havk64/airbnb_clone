from base import BaseTestCase
from app.models.review import Review
from app.models.user import User
from fixtures import *

class ReviewTestCase(BaseTestCase):
    table = [User, Review]
    path = '/users/1/reviews'
    example = fixt_reviews[0]

    def test_create(self):
        count = 1
        for review in fixt_reviews:
            last_review = self.create_row(review, '201 CREATED')
            self.check(last_review.id == count)
            count += 1
        # It should return 404 if user_id is not found(GET)
        review_table = {'model': Review, 'path': '/users/42/reviews'}
        resp = self.app.get('/users/42/review', fixt_reviews[0])
        self.check(resp.status_code, 404)
        # It should return 404 if user_id is not found(POST)
        review_table = {'model': Review, 'path': '/users/42/reviews'}
        resp = self.app.post('/users/42/review', fixt_reviews[0])
        self.check(resp.status_code, 404)
        # Bad request
        # Duplicated

    def test_list(self):
        self.check_list()

    def test_get(self):
        self.check_get('Review')

    def test_delete(self):
        self.check_delete('Review')
