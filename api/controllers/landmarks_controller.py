import logging

from flask_restx import Resource

from models.models import landmark_model
from services.landmarks_service import init_service, get_landmark_by_id

LOG = logging.getLogger('Landmark Controller')

def init_landmarks_controller(app, api):
    ''' Configure landmark controller '''
    LOG.info('Starting Landmark Controller')
    landmarks_model = landmark_model(api)
    init_service(app)

    class Marker(Resource):
        '''Controller for a landmark'''
        @api.marshal_with(landmarks_model)
        def get(self, tour_id):
            try:
                marker = get_landmark_by_id(tour_id)
                if marker is not None:
                    return marker, 200
                return 'not exist', 404
            except:
                LOG.error('Landmark not found')
                return None, 404

    # Handle landmark collections
    api.add_resource(Marker, '/api/v1/tours/<string:tour_id>/tourview')
