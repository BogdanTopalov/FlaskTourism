import json

from tests.base import BaseTestClass, generate_token
from tests.factory_config import UserFactory


class TestUserAuthentication(BaseTestClass):
    def test_user_registration(self):
        result = self.client.post(
            '/register',
            headers={
                "Content-Type": "application/json"
            },
            data=json.dumps({
                "first_name": "AAA",
                "last_name": "BBB",
                "email": "abv@abv.bg",
                "password": "alabala1"
            })
        )

        self.assertTrue(result.status_code == 200)

    def test_user_registration_with_short_password(self):
        result = self.client.post(
            '/register',
            headers={
                "Content-Type": "application/json"
            },
            data=json.dumps({
                "first_name": "AAA",
                "last_name": "BBB",
                "email": "abv@abv.bg",
                "password": "a2"
            })
        )

        self.assertTrue(result.status_code == 400)
        self.assertTrue(result.json['message']['password'] == ['Password must be 6 or more characters'])

    def test_user_registration_with_invalid_password(self):
        result = self.client.post(
            '/register',
            headers={
                "Content-Type": "application/json"
            },
            data=json.dumps({
                "first_name": "AAA",
                "last_name": "BBB",
                "email": "abv@abv.bg",
                "password": "aaaaaaaaaaa"
            })
        )

        self.assertTrue(result.status_code == 400)
        self.assertTrue(
            result.json['message']['password'] == ['Password must not contain only letters or only numbers']
        )

    def test_user_registration_with_invalid_email(self):
        result = self.client.post(
            '/register',
            headers={
                "Content-Type": "application/json"
            },
            data=json.dumps({
                "first_name": "AAA",
                "last_name": "BBB",
                "email": "123",
                "password": "alabala1"
            })
        )

        self.assertTrue(result.status_code == 400)
        self.assertTrue(
            result.json['message']['email'] == ['Email is not in valid format']
        )

    def test_user_registration_with_existing_email(self):
        user = UserFactory(email='abv@abv.bg')

        result = self.client.post(
            '/register',
            headers={
                "Content-Type": "application/json"
            },
            data=json.dumps({
                "first_name": "AAA",
                "last_name": "Bb",
                "email": "abv@abv.bg",
                "password": "alabala1"
            })
        )

        self.assertTrue(result.status_code == 400)
        self.assertTrue(result.json['message'] == 'Try again with another email')

    def test_user_login(self):
        self.client.post(
            '/register',
            headers={
                "Content-Type": "application/json"
            },
            data=json.dumps({
                "first_name": "AAA",
                "last_name": "Bb",
                "email": "abv@abv.bg",
                "password": "alabala1"
            })
        )

        result = self.client.post(
            '/login',
            headers={
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "email": "abv@abv.bg",
                "password": "alabala1"
            })
        )

        self.assertTrue(result.status_code == 200)

    def test_user_login_with_invalid_email(self):
        self.client.post(
            '/register',
            headers={
                "Content-Type": "application/json"
            },
            data=json.dumps({
                "first_name": "AAA",
                "last_name": "Bb",
                "email": "abv@abv.bg",
                "password": "alabala1"
            })
        )

        result = self.client.post(
            '/login',
            headers={
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "email": "1",
                "password": "alabala1"
            })
        )

        self.assertTrue(result.status_code == 400)
        self.assertTrue(
            result.json['message']['email'] == ['Email is not in valid format']
        )

    def test_user_login_with_invalid_password(self):
        self.client.post(
            '/register',
            headers={
                "Content-Type": "application/json"
            },
            data=json.dumps({
                "first_name": "AAA",
                "last_name": "Bb",
                "email": "abv@abv.bg",
                "password": "alabala1"
            })
        )

        result = self.client.post(
            '/login',
            headers={
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "email": "aaa@bbb.cc",
                "password": "123123123"
            })
        )

        self.assertTrue(result.status_code == 400)
        self.assertTrue(
            result.json['message']['password'] == ['Password must not contain only letters or only numbers']
        )

    def test_user_login_with_short_password(self):
        self.client.post(
            '/register',
            headers={
                "Content-Type": "application/json"
            },
            data=json.dumps({
                "first_name": "AAA",
                "last_name": "Bb",
                "email": "abv@abv.bg",
                "password": "alabala1"
            })
        )

        result = self.client.post(
            '/login',
            headers={
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "email": "aaa@bbb.cc",
                "password": "asd1"
            })
        )

        self.assertTrue(result.status_code == 400)
        self.assertTrue(
            result.json['message']['password'] == ['Password must be 6 or more characters']
        )

    def test_user_login_with_invalid_credentials(self):
        self.client.post(
            '/register',
            headers={
                "Content-Type": "application/json"
            },
            data=json.dumps({
                "first_name": "AAA",
                "last_name": "Bb",
                "email": "abv@abv.bg",
                "password": "alabala1"
            })
        )

        result = self.client.post(
            '/login',
            headers={
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "email": "aaa@bbb.cc",
                "password": "alabala2"
            })
        )

        self.assertTrue(result.status_code == 400)
        self.assertTrue(result.json['message'] == 'Invalid credentials')

    def test_user_details_with_valid_token(self):
        user = UserFactory()
        token = generate_token(user)

        result = self.client.post(
            '/user',
            headers={
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "token": token
            })
        )

        self.assertTrue(result.status_code == 200)
        self.assertTrue(result.json['id'] == user.id)
        self.assertTrue(result.json['first_name'] == user.first_name)
        self.assertTrue(result.json['last_name'] == user.last_name)
        self.assertTrue(result.json['email'] == user.email)

    def test_user_details_with_invalid_token(self):
        user = UserFactory()

        result = self.client.post(
            '/user',
            headers={
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "token": "123"
            })
        )

        self.assertTrue(result.status_code == 401)
        self.assertTrue(result.json['message'] == 'Token can not be verified')
