from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from users import serializers


class UsersRegister(APIView):
    def post(self, request):
        """
        회원가입
        POST /api/v1/users/register/
        """
        serializer = serializers.UsersRegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data.get("password"))
            user.save()
            serializer = serializers.UsersRegisterSerializer(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
