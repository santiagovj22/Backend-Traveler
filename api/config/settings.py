import os

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

DB_TRAVELER_CONNECTION = os.environ.get('DB_TRAVELER_CONNECTION')
JWT_IDENTITY_CLAIM = os.environ.get('JWT_IDENTITY_CLAIM')
JWT_ALGORITHM = os.environ.get('JWT_ALGORITHM')
JWT_DECODE_AUDIENCE = os.environ.get('JWT_DECODE_AUDIENCE')
PUBLIC_KEY = open('pubkey.pem').read()
