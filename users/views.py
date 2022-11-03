from django.contrib.auth import authenticate, login
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


class Login(APIView):
    def post(self, request):
        """
        로그인
        POST /api/v1/users/login/
        """
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return Response(
                {"status": True, "message": "Login Success"}, status=status.HTTP_200_OK
            )
        return Response({"status": False}, status=status.HTTP_404_NOT_FOUND)
