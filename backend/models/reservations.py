from datetime import datetime

from db import db
from models.enums import Status


class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nights = db.Column(db.Integer, nullable=False)
    status = db.Column(
        db.Enum(Status),
        default=Status.pending,
        nullable=False
    )
    created_on = db.Column(
        db.DateTime,
        default=datetime.utcnow(),
        nullable=False
    )
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
