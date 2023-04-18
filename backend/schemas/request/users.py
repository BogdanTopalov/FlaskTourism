from marshmallow import fields, validate

from schemas.base import UserRequestBaseSchema


class UserRegisterSchema(UserRequestBaseSchema):
    first_name = fields.String(
        required=True,
        validate=validate.And(
            validate.Length(min=2, max=50),
            validate.ContainsNoneOf(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']))
    )
    last_name = fields.String(
        required=True,
        validate=validate.And(
            validate.Length(min=2, max=50),
            validate.ContainsNoneOf(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']))
    )


class UserLoginSchema(UserRequestBaseSchema):
    pass
