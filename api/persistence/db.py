import logging

from persistence.mongo_db import DatabaseConnection

DB = DatabaseConnection()

LOG = logging.getLogger('MongoDB')


def init_db(app):
    DB.init_db(app)


def get_tours_collection():
    return DB.get_collection('tours')


def get_users_collection():
    return DB.get_collection('users')


def get_landmarks_collection():
    return DB.get_collection('landmarks')


def get_experiences_collections():
    return DB.get_collection('experiences')
