import logging
from bson import ObjectId

from persistence.db import get_tours_collection

LOG = logging.getLogger('Tours Dao')


def create_tour(tour):
    tour = get_tours_collection().insert_one(tour)
    return tour


def get_all_tours(search_term, skip, limit):
    '''Rows for all tours records'''
    LOG.debug('search = %s', search_term)
    LOG.debug('pagination skip= %s limit=%s', skip, limit)
    try:
        if search_term:
            query = {'$or': [{'location': {'$regex': search_term, '$options': 'i'}},
                             {'title': {'$regex': search_term, '$options': 'i'}},
                             {'brief': {'$regex': search_term, '$options': 'i'}}
                             ]
                     }

            rows = get_tours_collection().count_documents(query)
            return [row for row in get_tours_collection().find(query).sort('location')], rows

        rows = get_tours_collection().count_documents({})
        return [row for row in get_tours_collection().find().sort('location').skip(skip).limit(limit)], rows
    except Exception:
        LOG.exception('Error Connect to DB at get all tours', exc_info=True)
        return None


def get_tour(_id):
    '''Rows for specific tour'''
    try:
        return get_tours_collection().find_one({'_id': ObjectId(_id)})
    except Exception:
        LOG.error('Error Connect to DB at get a tour', exc_info=True)
        return None
