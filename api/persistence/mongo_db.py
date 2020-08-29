import logging

from flask_pymongo import PyMongo
from pymongo_inmemory import MongoClient

LOG = logging.getLogger('Database Connection')
class DatabaseConnection:
    ready = False
    db = None

    def init_db(self, app):
        isTest = app.config['IS_TEST']
        if not self.ready:
            self.ready = True
            if isTest:
                LOG.info('Start test database')
                self.db = MongoClient()['testdb']
            else:
                LOG.info('Start production database')
                self.db = PyMongo(app).db

    def get_collection(self, name):
        return self.db[name]
