import json

from models import RoleType
from tests.base import BaseTestClass, generate_token
from tests.factory_config import UserFactory, HotelFactory


class TestHotelModel(BaseTestClass):
    def test_adding_a_hotel(self):
        user = UserFactory(role=RoleType.admin)
        token = generate_token(user)

        result = self.client.post(
            '/hotels/add',
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}",
            },
            data=json.dumps({
                "country": "BG",
                "name": "Hotel C",
                "stars": 4,
                "price_per_night": 5.0,
                "city": "Sofia",
                "image_url": "https://images.unsplash.com/"
                             "photo-1584132967334-10e028bd69f7?ixlib"
                             "=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto"
                             "=format&fit=crop&w=1170&q=80"
            })
        )

        self.assertTrue(result.status_code == 201)
        self.assertTrue(result.json == {
            "id": 1,
            "country": "BG",
            "name": "Hotel C",
            "stars": 4,
            "price_per_night": 5.0,
            "city": "Sofia",
            "image_url": "https://images.unsplash.com/"
                         "photo-1584132967334-10e028bd69f7?ixlib"
                         "=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto"
                         "=format&fit=crop&w=1170&q=80"
        })

    def test_adding_hotel_with_regular_user(self):
        user = UserFactory()
        token = generate_token(user)

        result = self.client.post(
            '/hotels/add',
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}"
            },
            data=json.dumps({
                "country": "BG",
                "name": "Hotel C",
                "stars": 4,
                "price_per_night": 5.0,
                "city": "Sofia",
                "image_url": "https://images.unsplash.com/"
                             "photo-1584132967334-10e028bd69f7?ixlib"
                             "=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto"
                             "=format&fit=crop&w=1170&q=80"
            })
        )

        self.assertTrue(result.status_code == 403)
        self.assertTrue(result.json['message'] == "You don't have permission for this action")

    def test_updating_hotel(self):
        hotel = HotelFactory(country='Spain', city='Barcelona')
        user = UserFactory(role=RoleType.admin)
        token = generate_token(user)

        result = self.client.put(
            f'/hotels/update/{hotel.id}',
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}"
            },
            data=json.dumps({
                "country": "Bulgaria",
                "name": hotel.name,
                "stars": hotel.stars,
                "price_per_night": hotel.price_per_night,
                "city": "Sofia",
                "image_url": hotel.image_url
            })
        )

        self.assertTrue(result.status_code == 200)
        self.assertTrue(result.json['country'] == 'Bulgaria')
        self.assertTrue(result.json['city'] == 'Sofia')

    def test_updating_hotel_that_does_not_exist(self):
        hotel = HotelFactory(country='Spain', city='Barcelona')
        user = UserFactory(role=RoleType.admin)
        token = generate_token(user)

        result = self.client.put(
            f'/hotels/update/123',
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}"
            },
            data=json.dumps({
                "country": "Bulgaria",
                "name": hotel.name,
                "stars": hotel.stars,
                "price_per_night": hotel.price_per_night,
                "city": "Sofia",
                "image_url": hotel.image_url
            })
        )

        self.assertTrue(result.status_code == 400)
        self.assertTrue(result.json['message'] == "Hotel with id:123 does not exist")

    def test_updating_hotel_with_regular_user(self):
        hotel = HotelFactory(country='Spain', city='Barcelona')
        user = UserFactory()
        token = generate_token(user)

        result = self.client.put(
            f'/hotels/update/{hotel.id}',
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}"
            },
            data=json.dumps({
                "country": "Bulgaria",
                "name": hotel.name,
                "stars": hotel.stars,
                "price_per_night": hotel.price_per_night,
                "city": "Sofia",
                "image_url": hotel.image_url
            })
        )

        self.assertTrue(result.status_code == 403)
        self.assertTrue(result.json['message'] == "You don't have permission for this action")

    def test_deleting_hotel(self):
        hotel = HotelFactory()
        user = UserFactory(role=RoleType.admin)
        token = generate_token(user)

        result = self.client.delete(
            f'/hotels/delete/{hotel.id}',
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}"
            }
        )

        self.assertTrue(result.status_code == 200)
        self.assertTrue(result.json['message'] == 'Hotel deleted successfully')

    def test_deleting_hotel_with_regular_user(self):
        hotel = HotelFactory()
        user = UserFactory()
        token = generate_token(user)

        result = self.client.delete(
            f'/hotels/delete/{hotel.id}',
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}"
            }
        )

        self.assertTrue(result.status_code == 403)
        self.assertTrue(result.json['message'] == "You don't have permission for this action")

    def test_deleting_hotel_that_does_not_exist(self):
        hotel = HotelFactory()
        user = UserFactory(role=RoleType.admin)
        token = generate_token(user)

        result = self.client.delete(
            f'/hotels/delete/123',
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}"
            }
        )

        self.assertTrue(result.status_code == 400)
        self.assertTrue(result.json['message'] == "Hotel with id:123 does not exist")

    def test_getting_all_hotels(self):
        hotel_1 = HotelFactory()
        hotel_2 = HotelFactory()

        result = self.client.get('/hotels')

        self.assertTrue(result.status_code == 200)
        self.assertTrue(len(result.json) == 2)
        self.assertTrue(result.json[0]['stars'] == 4)
        self.assertTrue(result.json[0]['price_per_night'] == 100.0)

    def test_getting_single_hotel(self):
        hotel = HotelFactory()
        user = UserFactory()
        token = generate_token(user)

        result = self.client.get(
            f'/hotels/{hotel.id}',
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}"
            }
        )

        self.assertTrue(result.status_code == 200)

    def test_getting_single_hotel_that_does_not_exist(self):
        hotel = HotelFactory()
        user = UserFactory()
        token = generate_token(user)

        result = self.client.get(
            f'/hotels/123',
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}"
            }
        )

        self.assertTrue(result.status_code == 400)
        self.assertTrue(result.json['message'] == "Hotel with id:123 does not exist")

    def test_getting_single_hotel_unauthenticated(self):
        hotel = HotelFactory()

        result = self.client.get(f'/hotels/{hotel.id}')

        self.assertTrue(result.status_code == 401)
        self.assertTrue(result.json['message'] == 'Token can not be verified')
