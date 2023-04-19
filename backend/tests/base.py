from flask_testing import TestCase

from app_config import create_app
from db import db
from managers.auth_manager import AuthManager


def generate_token(user):
    return AuthManager.encode_token(user)


class BaseTestClass(TestCase):
    def create_app(self):
        return create_app('TEST_CONFIG_OBJECT')

    def setUp(self):
        db.init_app(self.app)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
