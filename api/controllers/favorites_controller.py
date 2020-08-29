import logging

from flask_restx import Resource
from flask import request
from flask_jwt_extended import jwt_required, get_current_user

from models.models import tour_model
from services.favorites_service import init_service, add_favorites, get_favorite_tours, remove_favorite

LOG = logging.getLogger('Favorites Controller')

def init_favorites_controller(app, api):

    init_service(app)

    LOG.info('Favorite tours')
    tours_model = tour_model(api)

    class FavoriteTours(Resource):
        '''Controller for favorites'''
        @jwt_required
        def post(self, user_id):
            LOG.info('Add to favorites')
            try:
                tour = request.get_json()
                user = get_current_user()

                # This action cant be only execute by current user
                if user_id != user['user_id']:
                    return None, 401

                add_favorites(tour, user_id)
                return None, 201
            except:
                LOG.exception('Error Creating favorites ')
                return None, 400

        @jwt_required
        @api.marshal_with(tours_model)
        def get(self, user_id):
            LOG.info('Get favorites')
            try:
                user = get_current_user()
                if user_id != user['user_id']:
                    return None, 401

                favorites_list = get_favorite_tours(user_id)
                return favorites_list, 200
            except:
                LOG.exception('Error to get favorites')
                return None, 400

        @jwt_required
        def delete(self, user_id):
            '''Delete favorite'''
            try:
                tour = request.get_json()
                user = get_current_user()
                if user_id != user['user_id']:
                    return None, 401
                return remove_favorite(tour, user_id), 200
            except:
                LOG.exception('Error to delete favorite')
                return None, 400

    api.add_resource(FavoriteTours, '/api/v1/users/<string:user_id>/favorites')
