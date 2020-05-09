from persistence.db import init_db

from persistence.tours_dao import get_all_tours, get_tour

def init_service(app):
    '''Configure service for tours'''
    # Init database
    init_db(app)

def get_tours():
    '''Returns a tours collection'''
    return get_all_tours()


def get_tour_by_id(tourid):
    '''Return a tour by id'''
    return get_tour(tourid)
