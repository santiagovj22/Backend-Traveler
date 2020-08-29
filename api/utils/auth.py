from flask_jwt_extended import JWTManager, get_raw_jwt

def configure_jwt(app):
    # pylint: disable=W0612
    jwt = JWTManager(app)
    @jwt.user_loader_callback_loader
    def user_loader_callback(identity):
        token = get_raw_jwt()
        return {'user_id' : token['sub'], 'name': token['name'], 'email': token['email']}
