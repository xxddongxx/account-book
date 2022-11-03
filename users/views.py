from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from users import serializers
from users.models import User


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
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


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


class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        로그아웃
        POST /api/v1/users/logout/
        """
        logout(request)
        return Response(
            {"status": True, "message": "Logout Success"}, status=status.HTTP_200_OK
        )


class UsersDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        """
        회원 정보
        GET /api/v1/users/{pk}/
        """
        user = User.objects.get(pk=pk)
        serializer = serializers.UsersSerializer(user)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UsersView(APIView):
    permission_classes = [IsAdminUser]
    """
    회원 목록
    GET /api/v1/users/
    """

    def get(self, request):
        users = User.objects.all()
        serializer = serializers.UsersSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
