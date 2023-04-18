from marshmallow import fields

from schemas.base import HotelBaseSchema


class HotelResponseSchema(HotelBaseSchema):
    id = fields.Integer(required=True)
