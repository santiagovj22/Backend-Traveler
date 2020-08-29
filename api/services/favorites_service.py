import logging

from persistence.users_dao import add_to_favorites, favorite_exists, get_favorites, remove_favorite_tour
from persistence.db import init_db

LOG = logging.getLogger('Favorites Service')

def init_service(app):
    LOG.info('Start Favorites service')
    init_db(app)

def add_favorites(tour, user_id):
    '''Saved tour into favorites if not exists'''
    LOG.info('favorites into service')
    tour_id = tour['tourId']
    if not favorite_exists(tour_id, user_id):
        LOG.debug('Favorite will be added')
        add_to_favorites(tour_id, user_id)
    else:
        LOG.debug('favorite already exist')

def get_favorite_tours(user_id):
    return get_favorites(user_id)

def remove_favorite(tour_id, user_id):
    tour = tour_id['tourId']
    remove_favorite_tour(tour, user_id)
