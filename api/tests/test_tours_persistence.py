import unittest
from bson import ObjectId
from flask import Flask

from persistence.db import init_db
from persistence.tours_dao import get_all_tours, get_tour, create_tour

app = Flask("test")
app.config['IS_TEST'] = True

class PersistenceToursTests(unittest.TestCase):
    def setUp(self):
        init_db(app)

    def test_can_create_tour(self):
        tour = create_tour({'title':'Cochabamba', 'description': 'Este tour es para tests'})
        self.assertIsNotNone(tour)

    def test_can_read_tours_from_db(self):
        tours, _ = get_all_tours(None, 1, 5)
        self.assertIsNotNone(tours)

    def test_can_search_tour_on_db(self):
        search_term = 'Cochabamba'
        tours, rows = get_all_tours(search_term, None, None)
        self.assertIsNotNone(tours)
        self.assertEqual(len(tours), rows)

    def test_can_paginated_tour_on_db(self):
        skip = 1
        limit = 5
        tours, _ = get_all_tours(None, skip, limit)
        self.assertIsNotNone(tours)

    def test_cannot_read_inexistent_tour(self):
        empty = ObjectId("000000000000000000000000")
        tour = get_tour(empty)
        self.assertIsNone(tour)

if __name__ == '__main__':
    unittest.main()
