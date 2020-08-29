import logging
import re

from persistence.db import init_db
from persistence.tours_dao import get_all_tours, get_tour
from utils.sanitization import sanitize_pagination

LOG = logging.getLogger('Tours Service')


def init_service(app):
    '''Configure service for tours'''
    LOG.info('Starting tours service')
    # Init database
    init_db(app)


def get_tours(search_term, page, limit):
    '''Returns a tours collection'''
    sanitized_page, sanitized_limit, skip = sanitize_pagination(page, limit)
    tours, rows = get_all_tours(sanitize_search(search_term), skip, limit)
    return tours, rows, sanitized_page, sanitized_limit

def get_tour_by_id(tour_id):
    '''Return a tour by id'''
    return get_tour(tour_id)

def sanitize_search(search_term):
    if search_term is None:
        return None
    search_value = re.sub(r'[^a-zA-Z0-9 \n\.]', r'', search_term)
    return search_value
