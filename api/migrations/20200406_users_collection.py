"""2020-06-04 migration"""

name = "20200406_users_collection"
dependencies = ['20201105_initial']

def upgrade(db):
    db.create_collection('users')
