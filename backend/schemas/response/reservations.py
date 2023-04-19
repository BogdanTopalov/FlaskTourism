from marshmallow import fields

from schemas.base import ReservationBaseSchema


class ReservationResponseSchema(ReservationBaseSchema):
    id = fields.Integer(required=True)
