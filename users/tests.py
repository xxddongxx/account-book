from django.urls import reverse
from rest_framework import status, response
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import Token

from users.models import User


class AccountTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        data = {"username": "test@test.com", "password": "testpw"}
        user = User.objects.create_user(username="test@test.com", password="testpw")
        print("===================user=================", user.username)
        response = self.client.post("/api/v1/users/login/", data=data, format="json")

        refresh = response.data.get("refresh")
        access = response.data.get("access")
        refresh_response = self.client.post(
            "/api/v1/users/login/", data={"refresh": refresh}, format="json"
        )
        print("===============refresh_response==============", refresh_response)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Log out
        self.client.logout()

        # url = reverse("register")
        # print("url >>> ", url)
        #
        # data = {"username": "test@test.com", "password": "testpw"}
        # response = self.client.post(url, data, format="json")
        # print("response >>> ", response)
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(User.objects.count(), 1)
        # self.assertEqual(User.objects.get().username, "test@test.com")

        # Include an appropriate `Authorization:` header on all requests.
        # token = Token.objects.get(user__username="lauren")
        # client = APIClient()
        # client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
