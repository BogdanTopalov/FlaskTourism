from datetime import datetime

from db import db


class Hotel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    stars = db.Column(db.Integer, nullable=False)
    country = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    price_per_night = db.Column(db.Float, nullable=False)
    added_on = db.Column(
        db.DateTime,
        default=datetime.utcnow(),
        nullable=False
    )
    reservations = db.relationship('Reservation', backref='hotel')
