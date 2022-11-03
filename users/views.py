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
        TODO Token
        if serializer.is_valid(raise_exception=False):
            user = serializer.save()
            # jwt token 접근해주기
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            response = {
                "user": serializer.data,
                "message": "register successs",
                "token": {
                    "access": access_token,
                    "refresh": refresh_token,
                },
            }
            return Response(
                response,
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        """
        serializer = serializers.UsersRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data.get('password'))
            user.save()
            serializer = serializers.UsersRegisterSerializer(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    def post(self, request):
        """
        로그인
        POST /api/v1/users/login/
        TODO Token
        user = authenticate(username=request.data.get("username"), password=request.data.get("password"))
        if user is not None:
            serializer = serializers.LoginSerializer(user)
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token)
            response = {
                "user": serializer.data,
                "message": "login success",
                "token": {
                    "access": access_token,
                    "refresh": refresh_token,
                },
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
        """
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return Response({"status": True, "message": "Success"}, status=status.HTTP_200_OK)
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
