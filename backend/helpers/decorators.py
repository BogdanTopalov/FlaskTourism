from flask import request
from werkzeug.exceptions import BadRequest, Forbidden

from managers.auth_manager import auth


def validate_schema(schema_name):
    def decorated_function(func):
        def wrapper(*args, **kwargs):
            schema = schema_name()
            data = request.get_json()
            errors = schema.validate(data)

            if not errors:
                return func(*args, **kwargs)

            raise BadRequest(errors)
        return wrapper
    return decorated_function


def permission_required(role):
    def decorated_function(func):
        def wrapper(*args, **kwargs):
            current_user = auth.current_user()

            if current_user.role == role:
                return func(*args, **kwargs)

            raise Forbidden("You don't have permission for this action")
        return wrapper
    return decorated_function
