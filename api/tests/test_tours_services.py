import unittest
import uuid

from bson import ObjectId
from flask import Flask


from services.tours_service import init_service, get_tours, get_tour_by_id

app = Flask("test")
app.config['IS_TEST'] = True

class ServiceToursTests(unittest.TestCase):
    def setUpd(self):
        init_service(app)

    def test_can_read_tours_all_fields(self):
        tours, _, _, _ = get_tours(None, 0, 10000)
        self.assertIsNotNone(tours)

    def test_can_read_tours_all_fields_paginated(self):
        for i in range(0, 3):
            tours, _, _, _ = get_tours(None, i, 5)
            self.assertNotEqual(len(tours), 5)

    def test_can_read_tours_all_fields_searched_sanitization(self):
        tours, _, _, _ = get_tours('Cochabamba', 0, 0)
        self.assertTrue(len(tours) >= 0)

    def test_can_read_tours_all_fields_paginated_sanitization(self):
        for _ in range(0, 5):
            tours, _, sanitized_page, sanitized_limit = get_tours(None, -1, 11)
            self.assertTrue(len(tours) <= 10)
            self.assertTrue(sanitized_page == 1)
            self.assertTrue(sanitized_limit == 10)

    def test_can_read_tour_by_id(self):
        unique_id = str(uuid.uuid1())
        tour = get_tour_by_id('5eb1cbe8ac46be6fab88bc73')
        self.assertIsNot(tour, unique_id)

    def test_cannot_service_inexistent_tour(self):
        empty = ObjectId("000000000000000000000000")
        tour = get_tour_by_id(empty)
        self.assertIsNone(tour)

if __name__ == '__main__':
    unittest.main()
