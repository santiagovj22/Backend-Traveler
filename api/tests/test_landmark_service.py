import unittest

from bson import ObjectId
from flask import Flask

from services.landmarks_service import init_service, get_landmark_by_id

app = Flask("test")
app.config['IS_TEST'] = True

class ServiceLandmarkTest(unittest.TestCase):
    def setUp(self):
        init_service(app)

    def test_can_read_landmark_by_id(self):
        tour_id = '5eeb86c96d5f80c5f2fdbb00'
        landmark = get_landmark_by_id(tour_id)
        self.assertIsNot(landmark, tour_id)

    def test_cannot_service_inexistent_landmark(self):
        empty = ObjectId('000000000000000000000000')
        landmark = get_landmark_by_id(empty)
        self.assertIsNone(landmark, empty)

if __name__ == '__main__':
    unittest.main()
