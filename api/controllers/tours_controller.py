import logging

from flask_restx import Resource, marshal

from models.models import tour_model

from services.tours_service import init_service, get_tours, get_tour_by_id

from utils.get_parser_data import get_parser_data

LOG = logging.getLogger('Tours Controller')

def init_tours_controller(app, api):
    ''' Configure tours controller '''
    LOG.info('Starting Tours Controller')
    tours_model = tour_model(api)
    init_service(app)

    class TourList(Resource):
        '''Represents a Rest resource to handle a tours collection'''
        def get(self):
            try:
                tours, rows, page, limit = get_parser_data(get_tours, None)
                tours_json = marshal(tours, tours_model, skip_none=True)
                return {'data': tours_json, 'page': page, 'limit': limit, 'totalRows': rows}, 200
            except:
                LOG.error('Error getting all tours')
                return None, 404

    class Tour(Resource):
        '''Controller for a tour'''
        @api.marshal_with(tours_model)
        def get(self, tour_id):
            try:
                tour = get_tour_by_id(tour_id)
                if tour is not None:
                    return tour, 200
                return 'not exist', 404
            except:
                LOG.error('Error getting a tour')
                return None, 404

    # Handle tours collections
    api.add_resource(TourList, '/api/v1/tours')
    api.add_resource(Tour, '/api/v1/tours/<string:tour_id>')
