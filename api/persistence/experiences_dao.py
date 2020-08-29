import logging

from persistence.db import get_experiences_collections

LOG = logging.getLogger('Experiences Tour Dao')

def get_tour_experiences(tour_id, skip, limit):
    LOG.debug('tour_id = %s', tour_id)
    LOG.debug('pagination skip= %s limit=%s', skip, limit)

    try:
        query = {'tour_id': tour_id}
        rows = get_experiences_collections().count_documents(query)
        return [row for row in get_experiences_collections().find(query).sort([('date', -1)]).skip(skip).limit(limit)], rows
    except Exception:
        LOG.exception('Error Connect to DB at get experiences ', exc_info=True)
        return None
