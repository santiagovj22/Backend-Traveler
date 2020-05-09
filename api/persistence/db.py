from flask_pymongo import PyMongo

__DB__ = {'ready': False, 'mongo': PyMongo(), 'tours': {}}

def init_db(app):
    '''Init conf database'''
    if not __DB__['ready']:
        __DB__['ready'] = True
        __DB__['mongo'].init_app(app)
        __DB__['tours'] = __DB__['mongo'].db.get_collection('tours')

def get_tours_collection():
    '''Get collection tours from db'''
    return __DB__['tours']
