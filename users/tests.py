from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User


class TestRegister(APITestCase):
    REGISTER_URL = "/api/v1/users/register/"

    def test_register_fail(self):
        """
        회원가입 실페 테스트
        """
        response = self.client.post(self.REGISTER_URL)
        response_data = response.json()

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIsInstance(response_data, dict)
        self.assertIn("message", response_data)

        response = self.client.post(self.REGISTER_URL, {"password": "test"})
        response_data = response.json()

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIsInstance(response_data, dict)
        self.assertIn("message", response_data)

    def test_register_success(self):
        """
        회원가입 성공 테스트
        """
        request_data = {
            "email": "test@test.com",
            "username": "test",
            "password": "test",
        }
        response = self.client.post(self.REGISTER_URL, request_data)
        response_data = response.json()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response_data, dict)
        self.assertIn("email", response_data)
        self.assertIn("username", response_data)
        self.assertNotIn("password", response_data)


class TestLogin(APITestCase):
    LOGIN_URL = "/api/v1/users/login/"

    def setUp(self):
        user = User.objects.create(email="test@test.com", username="test")
        user.set_password("test1234")
        user.save()
        self.user = user

    def test_login_fail(self):
        """
        로그인 실패 테스트
        """
        response = self.client.post(self.LOGIN_URL)
        response_data = response.json()

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIsInstance(response_data, dict)
        self.assertIn("message", response_data)

    def test_login_wrong_password(self):
        """
        비밀번호가 다른 실패 테스트
        """
        request_data = {"email": "test@test.com", "password": "1234"}
        response = self.client.post(self.LOGIN_URL, request_data)
        response_data = response.json()

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIsInstance(response_data, dict)
        self.assertIn("message", response_data)

    def test_login_success(self):
        """
        로그인 성공 테스트
        """
        request_data = {"email": "test@test.com", "password": "test1234"}
        response = self.client.post(self.LOGIN_URL, request_data)
        response_data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_data, dict)
        self.assertIn("message", response_data)
        self.assertIn("user", response_data)
        self.assertIn("token", response_data)
