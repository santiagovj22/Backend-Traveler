import logging

from persistence.db import init_db
from persistence.landmarks_dao import get_landmark

LOG = logging.getLogger('Landmark Service')

def init_service(app):
    '''Configure service for Landmark'''
    LOG.info('Starting landmark service')
    # Init database
    init_db(app)

def get_landmark_by_id(tour_id):
    '''Return tour view by id'''
    return get_landmark(tour_id)
