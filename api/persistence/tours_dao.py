from bson import ObjectId

from persistence.db import get_tours_collection

def get_all_tours():
    '''Rows for all tours records'''
    return  [row for row in get_tours_collection().find()]

def get_tour(_id):
    '''Rows for specific tour'''
    return get_tours_collection().find_one({'_id': ObjectId(_id)})
