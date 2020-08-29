import logging

from persistence.db import get_landmarks_collection

LOG = logging.getLogger('Landmark Dao')


def create_landmark(landmark):
    landmark = get_landmarks_collection().insert_one(landmark)
    return landmark


def get_landmark(tour_id):
    '''Get view for each Tour'''
    LOG.debug('tour_id = %s', tour_id)

    try:
        return get_landmarks_collection().find_one({'tourId': tour_id})
    except:
        LOG.error('Error Connecting the DB into landmark collection ')
        return None, 401
