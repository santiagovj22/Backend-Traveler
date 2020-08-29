import unittest
from bson import ObjectId

from flask import Flask
app = Flask("test")


class ApiTests(unittest.TestCase):
    def setUp(self):
        app.config['IS_TEST'] = True
        app.testing = True
        self.app = app.test_client()

    def test_get_tours_from_api(self):
        result = self.app.get('/api/v1/tours')
        self.assertIsNotNone(result)

    def test_get_tours_search(self):
        search_term = 'Cochabamba'
        result = self.app.get('/api/v1/tours?search=' + search_term)
        self.assertIsNotNone(result)

    def test_cannot_get_inexistent_tour(self):
        # We need create a random a value
        empty = ObjectId("000000000000000000000000")
        result = self.app.get(f'/api/v1/tours/{empty}')
        self.assertTrue(result.status_code == 404)

    def test_get_landmark_from_api(self):
        tour_id = ObjectId('5eeb86c96d5f80c5f2fdbb00')
        result = self.app.get(f'/api/v1/tours/{tour_id}/tourview')
        self.assertIsNotNone(result)

    def test_cannot_get_inexistent_landmark_from_api(self):
        empty = ObjectId('000000000000000000000000')
        result = self.app.get(f'/api/v1/tours/{empty}/tourview')
        self.assertTrue(result.status_code == 404)

    def test_get_tour_experiences(self):
        tour_id = ObjectId("5ec573d6fabc70e713595a94")
        result = self.app.get(f'/api/v1/tours/{tour_id}/experiences')
        self.assertIsNotNone(result)

    def test_cannot_get_tour_experiences(self):
        tour_id = 100000000085
        if tour_id.__int__() is True:
            result = self.app.get(f'/api/v1/tours/{tour_id}/experiences')
            self.assertEqual(result.status_code, 404)


if __name__ == '__main__':
    unittest.main()
