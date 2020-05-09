import logging
from flask_restx import Resource, fields

from services.tours_service import init_service, get_tours, get_tour_by_id

LOG = logging.getLogger('Tours Controller')

def init_tours_controller(app, api):
    ''' Configure tours controller '''
    LOG.debug('Starting Tours Controller')

    tour_model = api.model('Tour', {'_id': fields.String(), 'image': fields.String,
                                    'title':fields.String, 'brief': fields.String,
                                    'description': fields.String, 'location':fields.String,
                                    'duration': fields.String, 'transportType': fields.String,
                                    'rating':fields.Integer, 'ratingCount': fields.Integer})

    init_service(app)

    class TourList(Resource):
        '''Represents a Rest resource to handle a tours collection'''
        @api.marshal_with(tour_model)
        def get(self):
            ''' Return all list of tours '''
            LOG.debug('Called from the web')
            tours = get_tours()
            return tours

    class Tour(Resource):
        '''Controller for a tour'''
        @api.marshal_with(tour_model)
        def get(self, tourid):
            tour = get_tour_by_id(tourid)
            if tour is not None:
                return tour, 200
            api.abort(504, "Tour doesn't exist")

    # Handle tours collections
    api.add_resource(TourList, '/api/v1/tours')
    api.add_resource(Tour, '/api/v1/tours/<string:tourid>')
