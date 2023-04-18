from datetime import datetime, timedelta

import jwt
from decouple import config
from flask_httpauth import HTTPTokenAuth
from jwt import DecodeError
from werkzeug.exceptions import BadRequest, Unauthorized
from werkzeug.security import generate_password_hash, check_password_hash

from db import db
from models import User


class AuthManager:
    @staticmethod
    def register_user(user_data):
        user_data['password'] = generate_password_hash(user_data['password'])

        email_in_db = User.query.filter_by(email=user_data['email']).first()

        if email_in_db:
            raise BadRequest('Try again with another email')

        user = User(**user_data)

        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def login_user(user_data):
        user = User.query.filter_by(email=user_data['email']).first()

        if not user:
            raise BadRequest('Invalid credentials')

        if not check_password_hash(user.password, user_data['password']):
            raise BadRequest('Invalid credentials')

        return user

    @staticmethod
    def encode_token(user):
        payload = {
            'sub': user.id,
            'exp': datetime.utcnow() + timedelta(days=1)
        }
        token = jwt.encode(
            payload,
            key=config('JWT_KEY')
        )
        return token

    @staticmethod
    def decode_token(token):
        try:
            result = jwt.decode(
                token,
                key=config('JWT_KEY'),
                algorithms=['HS256']
            )
            return result
        except DecodeError as ex:
            raise BadRequest('Invalid or missing token')


auth = HTTPTokenAuth(scheme='Bearer')


@auth.verify_token
def verify_token(token):
    try:
        payload = AuthManager.decode_token(token)
        user = User.query.filter_by(id=payload['sub']).first()

        if not user:
            raise Unauthorized('Invalid or missing token')

        return user

    except Exception as ex:
        raise Unauthorized('Token can not be verified')
