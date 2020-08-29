import unittest

from flask import Flask

from persistence.db import init_db
from persistence.experiences_dao import get_tour_experiences

app = Flask("test")
app.config['IS_TEST'] = True

class PersistenceExperiencesTests(unittest.TestCase):
    def setUp(self):
        init_db(app)

    def test_can_read_experiences_from_db(self):
        tour_id = "5ec573d6f235901135952d3"
        experiences, _ = get_tour_experiences(tour_id, 1, 10)
        self.assertIsNotNone(experiences)
