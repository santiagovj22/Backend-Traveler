from flask_restx import fields, Api


def tour_model(api: Api):
    return api.model('Tour', {'_id': fields.String(), 'image': fields.String,
                              'title': fields.String, 'brief': fields.String,
                              'description': fields.String, 'location': fields.String,
                              'duration': fields.String, 'transportType': fields.String,
                              'rating': fields.Float, 'ratingCount': fields.Integer})


def auth_model(api: Api):
    return api.model('Auth', {'_id': fields.String, 'name': fields.String,
                              'email': fields.String, 'avatar': fields.String,
                              'tours': fields.List(fields.Nested(fields.String))})


def landmark_model(api: Api):
    location_fields = {'latitude': fields.Float, 'longitude': fields.Float}
    resource_fields = {'name': fields.String,
                       'type': fields.String, 'source': fields.String}
    landmarks_fields = {'idMarker': fields.String, 'category': fields.String,
                        'name': fields.String, 'number': fields.Integer,
                        'distance': fields.Float, 'description': fields.String,
                        'location': fields.Nested(location_fields), 'resources': fields.Nested(resource_fields)}
    return api.model('Landmark', {'_id': fields.String, 'tourId': fields.String,
                                  'landmarks': fields.List(fields.Nested(landmarks_fields))})


def experience_model(api: Api):
    resource_fields = {'type': fields.String, 'source': fields.String}
    return api.model('Experience', {'_id': fields.String, 'content': fields.String,
                                    'name': fields.String, 'rating': fields.Float,
                                    'resources': fields.List(fields.Nested(resource_fields)),
                                    'creationDate': fields.DateTime(), 'avatar': fields.String, })
