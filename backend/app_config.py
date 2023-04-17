from decouple import config
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api

from db import db
from routes import routes


DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASS')
DB_NAME = config('DB_NAME')
DB_PORT = config('DB_PORT')
TEST_DB_NAME = config('TEST_DB_NAME')


class DevelopmentConfig:
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (
        f'postgresql://{DB_USER}:{DB_PASSWORD}'
        f'@localhost:{DB_PORT}/{DB_NAME}'
    )


class TestingConfig:
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (
        f'postgresql://{DB_USER}:{DB_PASSWORD}'
        f'@localhost:{DB_PORT}/{TEST_DB_NAME}'
    )


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config(config_object))

    migrate = Migrate(app, db)
    api = Api(app)
    CORS(app)

    [api.add_resource(*route) for route in routes]

    return app
