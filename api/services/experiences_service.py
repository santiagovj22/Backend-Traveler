import logging

from persistence.db import init_db

from persistence.experiences_dao import get_tour_experiences

from utils.sanitization import sanitize_pagination

LOG = logging.getLogger('Experiences Service')

def init_service(app):
    '''Configure service for experiences'''
    LOG.info('Starting experiences service')
    # Init database
    init_db(app)

def get_experiences(tour_id, page, limit):
    '''Returns a experiences collection'''
    sanitized_page, sanitized_limit, skip = sanitize_pagination(page, limit)
    experiences, rows = get_tour_experiences(tour_id, skip, sanitized_limit)
    if experiences is None:
        experiences = []
    return experiences, rows, sanitized_page, sanitized_limit
