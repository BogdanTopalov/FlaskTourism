import re

from marshmallow import Schema, fields, validates, ValidationError, validate

from models import Status
from models.enums import RoleType


class UserRequestBaseSchema(Schema):
    email = fields.String(required=True)
    password = fields.String(required=True)

    @validates('email')
    def validate_email(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        if not re.fullmatch(regex, email):
            raise ValidationError('Email is not in valid format')

    @validates('password')
    def validate_password(self, password):
        if len(password) < 6:
            raise ValidationError('Password must be 6 or more characters')

        if password.isalpha() or password.isnumeric():
            raise ValidationError('Password must not contain only letters or only numbers')


class HotelBaseSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=2, max=150))
    stars = fields.Int(required=True, validate=validate.OneOf([1, 2, 3, 4, 5]))
    country = fields.Str(required=True, validate=validate.Length(min=2, max=50))
    city = fields.Str(required=True, validate=validate.Length(min=2, max=50))
    image_url = fields.Str(required=True)
    price_per_night = fields.Float(required=True)


class ReservationBaseSchema(Schema):
    status = fields.Enum(Status)
    created_on = fields.DateTime()
    user_id = fields.Int()
    hotel_id = fields.Int(required=True)
