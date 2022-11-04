from django.urls import reverse
from rest_framework import status, response
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import Token

from accounts.models import Account
from users.models import User


class AccountTests(APITestCase):
    register_url = "/api/v1/users/"

    def test_register(self):
        """
        회원가입 성공 테스트
        """

        data = {"username": "test@test.com", "password": "testpw"}
        response = self.client.post(self.register_url, data, format("json"))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.get().username, "test@test.com")

    def test_register_fail(self):
        """
        회원가입 실페 테스트
        """
        data = {"username": "test@test.com"}
        response = self.client.post(self.register_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
