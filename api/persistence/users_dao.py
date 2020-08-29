import logging

from bson import ObjectId
from persistence.db import get_users_collection, get_tours_collection

LOG = logging.getLogger('Users Dao')

def user_exists(user_id):
    '''Search for user'''
    LOG.info('Verify User Registered')
    previous_user = get_users_collection().find_one({'_id': user_id})
    return previous_user is not None

def create_user(user_id, user):
    '''Create a traveler user'''
    try:
        user['_id'] = user_id
        LOG.info('Insert User into DB')
        get_users_collection().insert_one(user)
        return user
    except:
        return None

def favorite_exists(tour_id, user_id):
    ''' favorites'''
    LOG.info('Check if favorite exist')
    user = get_users_collection().find_one({'_id': user_id})
    LOG.debug('User is %s and user_id is %s', user, user_id)
    if user is None:
        raise Exception('User does not exist')
    tour_exists = tour_id in user['favoriteTours']
    LOG.debug('Tour exists %s', tour_exists)

    return tour_exists

def add_to_favorites(tour_id, user_id):
    '''Add tour into favorites'''
    try:
        LOG.info('add tour to favorites')
        return get_users_collection().update_one({'_id': user_id}, {'$push': {'favoriteTours': tour_id}})
    except:
        LOG.info('Error to saved')
        return None

def get_favorites(user_id):
    '''Get list of tours favorites'''
    try:
        user = get_users_collection().find_one({'_id': user_id})
        favorite_list = user['favoriteTours']
        # convert each element of array to ObjectId for find information into tours collection
        favorite_ids = [ObjectId(x) for x in favorite_list]
        tours = get_tours_collection().find({'_id': {'$in': favorite_ids}})

        return [row for row in tours]

    except:
        LOG.exception('Error to get favorites')
        return None

def remove_favorite_tour(tour_id, user_id):
    '''Remove a favorite'''
    try:
        LOG.info('Remove tour from favorites')
        # The operator $pull delete the data with the method update_one
        return get_users_collection().update_one({'_id': user_id}, {'$pull': {'favoriteTours': {'$in' : [tour_id]}}})
    except:
        LOG.info('Error to delete')
        return None
