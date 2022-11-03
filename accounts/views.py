from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts import serializers


class Accounts(APIView):
    def post(self, request):
        """
        가계부 작성
        """
        serializer = serializers.AccountsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
