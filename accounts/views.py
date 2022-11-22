from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from accounts import serializers
from accounts.models import Account
from accounts.permissions import IsOwner


class Accounts(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwner]

    def post(self, request):
        """
        가계부 작성
        POST /api/v1/accounts/
        """
        serializer = serializers.AccountsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """
        가계부 목록
        GET /api/v1/accounts/
        """
        user = request.user

        if user.is_staff:
            accounts = Account.objects.filter(is_delete=False)
        else:
            accounts = Account.objects.filter(author=user, is_delete=False)

        serializer = serializers.AccountsSerializer(accounts, many=True)

        if serializer.data:
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_404_NOT_FOUND)


class AccountDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwner]

    def get_account(self, pk, author):
        return get_object_or_404(Account, pk=pk, author=author, is_delete=False)

    def get(self, request, pk):
        """
        가계부 상세
        GET /api/v1/accounts/<pk>/
        """
        user = request.user
        account = self.get_account(pk=pk, author=user)
        serializer = serializers.AccountsSerializer(account)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """
        가계부 수정
        PUT /api/v1/accounts/<pk>/
        """
        user = request.user
        account = self.get_account(pk=pk, author=user)
        serializer = serializers.AccountsSerializer(account, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        """
        가계부 삭제
        DELETE /api/v1/accounts/<pk>/
        """
        user = request.user
        account = self.get_account(pk=pk, author=user)
        account.is_delete = True
        account.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class AccountRestoration(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwner]

    def get(self, request):
        """
        가계부 삭제 항목
        GET /api/v1/accounts/restoration/
        """
        user = request.user
        if user.is_staff:
            accounts = Account.objects.filter(is_delete=True)
        else:
            accounts = Account.objects.filter(author=user, is_delete=True)

        serializer = serializers.AccountsSerializer(accounts, many=True)

        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class AccountRestorationDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwner]

    def get_account(self, pk, author):
        return get_object_or_404(Account, pk=pk, author=author, is_delete=True)

    def get(self, request, pk):
        """
        삭제된 가계부 상세
        GET /api/v1/accounts/restoration/<pk>/
        """
        user = request.user
        account = self.get_account(pk=pk, author=user)
        serializer = serializers.AccountsSerializer(account)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """
        삭제된 가계부 복구
        PUT /api/v1/accounts/restoration/<pk>/
        """
        user = request.user
        account = self.get_account(pk=pk, author=user)
        account.is_delete = False
        account.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
