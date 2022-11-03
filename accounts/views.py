from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts import serializers
from accounts.models import Account
from accounts.permissions import IsOwner


class Accounts(APIView):

    permission_classes = [IsOwner]

    def post(self, request):
        """
        가계부 작성
        POST /api/v1/accounts/
        """
        serializer = serializers.AccountsSerializer(data=request.data)
        print("serializer >>> ", repr(serializer))
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """
        가계부 목록
        GET /api/v1/accounts/
        """
        user = request.user
        accounts = Account.objects.filter(author=user)
        serializer = serializers.AccountsSerializer(accounts, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
