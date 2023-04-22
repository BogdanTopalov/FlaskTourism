import json

from models import RoleType
from tests.base import BaseTestClass, generate_token
from tests.factory_config import UserFactory, HotelFactory, ReservationFactory


class TestReservationModel(BaseTestClass):
    def test_creating_a_reservation(self):
        hotel = HotelFactory()
        user = UserFactory()
        token = generate_token(user)

        result = self.client.post(
            '/reservations/create',
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}",
            },
            data=json.dumps({
                "hotel_id": hotel.id,
                "nights": 3
            })
        )

        self.assertTrue(result.status_code == 200)

    def test_creating_a_reservation_unauthenticated(self):
        hotel = HotelFactory()

        result = self.client.post(
            '/reservations/create',
            headers={
                "Content-Type": "application/json",
                # "Authorization": f"Bearer {token}",
            },
            data=json.dumps({
                "hotel_id": hotel.id
            })
        )

        self.assertTrue(result.status_code == 401)
        self.assertTrue(result.json['message'] == 'Token can not be verified')

    def test_getting_all_reservations_with_regular_user(self):
        hotel = HotelFactory()
        user = UserFactory()
        token = generate_token(user)

        reservation_1 = ReservationFactory(user_id=user.id, hotel_id=hotel.id)
        reservation_2 = ReservationFactory(user_id=user.id, hotel_id=hotel.id)

        result = self.client.get(
            '/reservations',
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}",
            }
        )

        self.assertTrue(result.status_code == 403)
        self.assertTrue(result.json['message'] == "You don't have permission for this action")

    def test_getting_all_reservations_with_admin_user(self):
        hotel = HotelFactory()
        user = UserFactory(role=RoleType.admin)
        token = generate_token(user)

        reservation_1 = ReservationFactory(user_id=user.id, hotel_id=hotel.id)
        reservation_2 = ReservationFactory(user_id=user.id, hotel_id=hotel.id)

        result = self.client.get(
            '/reservations',
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}",
            }
        )

        self.assertTrue(result.status_code == 200)
        self.assertTrue(len(result.json) > 1)
