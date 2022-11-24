from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User


ACCOUNT_URL = "/api/v1/accounts/"
ACCOUNT_DELETE_LIST_URL = "/api/v1/accounts/restoration/"


def get_user():
    user = User.objects.create(email="test@test.com", username="test")
    user.set_password("test1234")
    user.save()
    return user


class TESTAccountsCreate(APITestCase):
    def setUp(self):
        self.user = get_user()

    def test_not_authorized(self):
        """
        비로그인(인증X) 가계부 생성 테스트
        """
        response = self.client.post(ACCOUNT_URL)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn("detail", data)

    def test_account_create_fail(self):
        """
        가계부 작성 실패 테스트
        """
        token = RefreshToken.for_user(self.user)
        header = {"HTTP_AUTHORIZATION": f"Bearer {token.access_token}"}
        response = self.client.post(ACCOUNT_URL, **header)
        response_data = response.json()

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIsInstance(response_data, dict)
        self.assertIn("message", response_data)

    def test_account_create_success(self):
        """
        가계부 작성 성공 테스트
        """
        token = RefreshToken.for_user(self.user)
        request_data = {"amount": 3500, "memo": "편의점 맥주"}
        header = {"HTTP_AUTHORIZATION": f"Bearer {token.access_token}"}
        response = self.client.post(ACCOUNT_URL, request_data, **header)
        response_data = response.json()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response_data, dict)
        self.assertIn("amount", response_data)
        self.assertIn("memo", response_data)
        self.assertIn("is_payment", response_data)
        self.assertIn("is_delete", response_data)


class TestGetAccounts(APITestCase):
    def setUp(self):
        self.user = get_user()

    def test_get_accounts_list(self):
        """
        가계부 목록 조회 성공 케이스
        """
        token = RefreshToken.for_user(self.user)
        request_data = {"amount": 3500, "memo": "편의점 맥주"}
        header = {"HTTP_AUTHORIZATION": f"Bearer {token.access_token}"}
        self.client.post(ACCOUNT_URL, request_data, **header)

        response = self.client.get(ACCOUNT_URL, **header)
        response_data = response.json()[0]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_data, dict)
        self.assertIn("amount", response_data)
        self.assertIn("memo", response_data)
        self.assertIn("is_payment", response_data)
        self.assertIn("is_delete", response_data)

    def test_accounts_delete(self):
        """
        가계부 삭제 성공 테스트
        """
        token = RefreshToken.for_user(self.user)
        request_data = {"amount": 3500, "memo": "편의점 맥주"}
        header = {"HTTP_AUTHORIZATION": f"Bearer {token.access_token}"}
        self.client.post(ACCOUNT_URL, request_data, **header)

        delete_accounts_url = ACCOUNT_URL + "1/"
        response = self.client.delete(delete_accounts_url, **header)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_accounts_delete_list(self):
        """
        가계부 삭제 목록 성공 테스트
        """
        token = RefreshToken.for_user(self.user)
        request_data = {"amount": 3500, "memo": "편의점 맥주", "is_delete": True}
        header = {"HTTP_AUTHORIZATION": f"Bearer {token.access_token}"}
        self.client.post(ACCOUNT_URL, request_data, **header)

        response = self.client.get(ACCOUNT_DELETE_LIST_URL, **header)
        response_data = response.json()[0]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_data, dict)
        self.assertIn("amount", response_data)
        self.assertIn("memo", response_data)
        self.assertIn("is_payment", response_data)
        self.assertIn("is_delete", response_data)

    def test_restoration_accounts(self):
        """
        가계부 삭제 복구 성공 테스트
        """
        token = RefreshToken.for_user(self.user)
        request_data = {"amount": 3500, "memo": "편의점 맥주", "is_delete": True}
        header = {"HTTP_AUTHORIZATION": f"Bearer {token.access_token}"}
        self.client.post(ACCOUNT_URL, request_data, **header)

        account_restoration_url = ACCOUNT_DELETE_LIST_URL + "1/"

        response = self.client.put(account_restoration_url, **header)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
