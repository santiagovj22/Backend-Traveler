import logging

from persistence.db import init_db
from persistence.users_dao import user_exists, create_user

LOG = logging.getLogger('Auth Service')

def init_service(app):
    '''Configure service for auth'''
    LOG.info('Starting users service')
    # Init database
    init_db(app)

def register_user(user_id, user):
    '''Create a user if it doesn't exist'''
    if not user_exists(user_id):
        return create_user(user_id, user)
    return user
