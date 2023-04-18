from flask import request
from flask_restful import Resource

from helpers.decorators import validate_schema
from managers.auth_manager import AuthManager
from schemas.request.users import UserRegisterSchema, UserLoginSchema
from schemas.response.users import UserResponseSchema


class RegisterResource(Resource):
    @validate_schema(UserRegisterSchema)
    def post(self):
        data = request.get_json()
        user = AuthManager.register_user(data)
        token = AuthManager.encode_token(user)
        return UserResponseSchema().dump({"token": token})


class LoginResource(Resource):
    @validate_schema(UserLoginSchema)
    def post(self):
        data = request.get_json()
        user = AuthManager.login_user(data)
        token = AuthManager.encode_token(user)
        return UserResponseSchema().dump({"token": token})
