from marshmallow import Schema, fields

from models.enums import RoleType


class UserResponseSchema(Schema):
    token = fields.Str(required=True)


class UserDetailsResponseSchema(Schema):
    id = fields.Int()
    first_name = fields.Str()
    last_name = fields.Str()
    email = fields.Email()
    role = fields.Enum(RoleType)
