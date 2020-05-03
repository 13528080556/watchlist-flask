
import os

PORT = 5000
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
                            os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'data.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
