from marshmallow import Schema, fields


class UserResponseSchema(Schema):
    token = fields.Str(required=True)
