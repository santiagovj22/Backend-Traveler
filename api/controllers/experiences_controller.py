import logging

from flask_restx import Resource, marshal

from services.experiences_service import init_service, get_experiences

from models.models import experience_model
from utils.get_parser_data import get_parser_data

LOG = logging.getLogger('Experiences Controller')

def init_experiences_controller(app, api):
    ''' Configure experiences controller '''
    LOG.info('Starting experiences Controller')
    experiences_model = experience_model(api)
    init_service(app)

    class Experiences(Resource):
        '''Represents a Rest resource to handle a experiences collection'''
        def get(self, tour_id):
            try:
                experiences, rows, page, limit = get_parser_data(get_experiences, tour_id)
                experiences_json = marshal(experiences, experiences_model, skip_none=True)
                return {'data': experiences_json, 'page': page, 'limit': limit, 'totalRows': rows}
            except:
                LOG.error('Not Found experiences')
                return None, 404

    api.add_resource(Experiences, '/api/v1/tours/<string:tour_id>/experiences')
