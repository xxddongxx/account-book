from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

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
        return Response(status=status.HTTP_404_NOT_FOUND)


class Logout(APIView):
    def post(self, request):
        """
        TODO
        로그아웃
        POST /api/v1/users/logout/
        """
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UsersDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        """
        TODO
        회원 정보
        GET /api/v1/users/{pk}/
        """
        user = User.objects.get(pk=pk)
        serializer = serializers.UsersSerializer(user)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UsersView(APIView):
    # permission_classes = [IsAdminUser]
    """
    TODO
    회원 목록
    GET /api/v1/users/
    """

    def get(self, request):
        users = User.objects.all()
        serializer = serializers.UsersSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
