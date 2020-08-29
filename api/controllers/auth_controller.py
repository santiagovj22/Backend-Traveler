import logging

from flask_restx import Resource
from flask import request
from flask_jwt_extended import decode_token

from models.models import auth_model
from services.auth_service import init_service, register_user

LOG = logging.getLogger('Auth Controller')

def init_auth_controller(main_app, api):
    ''' Configure Auth controller '''
    LOG.info('Starting Auth Controller')
    auths_model = auth_model(api)
    init_service(main_app)

    class Auth(Resource):
        '''A resource controller for Authentication'''
        @api.marshal_with(auths_model)
        def post(self):
            LOG.info('Entering to login user')
            try:
                LOG.info(request)
                data = request.get_json()
                LOG.info(data['token'])
                token_data = decode_token(data['token'], allow_expired=False)

                LOG.info(token_data)
                user = {
                    'email': token_data['email'],
                    'name': token_data['name'],
                    'picture': 'https://i.ibb.co/cwb773c/avatar-traveler.png',
                    'favoriteTours' :[],
                }
                if 'picture' in token_data:
                    user['avatar'] = token_data['picture']

                user_id = token_data['sub']
                traveler_user = register_user(user_id, user)

                return traveler_user
            except:
                LOG.error('Error validating token')
                return None, 401

    # Handle users collections
    api.add_resource(Auth, '/api/v1/auth/login')
