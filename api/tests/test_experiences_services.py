import unittest

from bson import ObjectId
from flask import Flask

from services.experiences_service import init_service, get_experiences

app = Flask("test")
app.config['IS_TEST'] = True

class ServiceExperiencesTests(unittest.TestCase):
    def setUpd(self):
        init_service(app)

    def test_can_show_all_experiences(self):
        tour_id = ObjectId("5ec573d6f235707135952a94")
        for i in range(0, 100):
            experiences, _, _, _ = get_experiences(tour_id, i, 10)
            self.assertIsNotNone(experiences)

    def test_cannot_show_any_experiences(self):
        tour_id = ObjectId("5ec573d6f235707135952a94")
        for i in range(0, 100):
            experiences, _, _, _ = get_experiences(tour_id, i, 10)
            if experiences is None:
                self.assertTrue(len(experiences) == 0)
