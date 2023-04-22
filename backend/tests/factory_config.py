from datetime import datetime

import factory

from db import db
from models import User, Hotel, Reservation
from models.enums import RoleType, Status


class BaseFactory(factory.Factory):
    @classmethod
    def create(cls, **kwargs):
        object = super().create(**kwargs)

        db.session.add(object)
        db.session.commit()

        return object


class UserFactory(BaseFactory):
    class Meta:
        model = User

    id = factory.Sequence(lambda x: x)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    password = factory.Faker('password')
    role = RoleType.regular


class HotelFactory(BaseFactory):
    class Meta:
        model = Hotel

    id = factory.Sequence(lambda x: x)
    name = factory.Faker('name')
    stars = 4
    country = factory.Faker('country')
    city = factory.Faker('city')
    image_url = factory.Faker('image_url')
    price_per_night = 100.0
    added_on = datetime.utcnow()


class ReservationFactory(BaseFactory):
    class Meta:
        model = Reservation

    id = factory.Sequence(lambda x: x)
    nights = 3
    status = Status.pending
    created_on = datetime.utcnow()
    user_id = 0
    hotel_id = 0
