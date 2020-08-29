import unittest

from flask import Flask

from persistence.db import init_db
from persistence.landmarks_dao import get_landmark, create_landmark

app = Flask("test")
app.config['IS_TEST'] = True

class PersistenceTestLandmarks(unittest.TestCase):
    def setUp(self):
        print('init')
        init_db(app)

    def test_can_create_tour(self):
        landmark = create_landmark({'tourId':'5eeb86c96d5f80c5f2fdbb00'})
        self.assertIsNotNone(landmark)

    def test_can_read_landmark_on_db(self):
        tour_id = '5eeb86c96d5f80c5f2fdbb00'
        landmark = get_landmark(tour_id)
        self.assertIsNotNone(landmark)

if __name__ == '__main__':
    unittest.main()
