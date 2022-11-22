from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
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
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    """
    로그인
    POST /api/v1/users/login/
    """

    def post(self, request):
        user = authenticate(
            email=request.data.get("email"), password=request.data.get("password")
        )
        if user is not None:
            serializer = serializers.UsersSerializer(user)
            token = TokenObtainPairSerializer.get_token(user)
            access_token = str(token.access_token)
            refresh_token = str(token)

            response = Response(
                {
                    "user": serializer.data,
                    "message": "Login Success",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )
            response.set_cookie(key="access", value=access_token, httponly=True)
            response.set_cookie(key="refresh", value=refresh_token, httponly=True)
            return response
        else:
            return Response(
                {"message": "Fail Login"}, status=status.HTTP_400_BAD_REQUEST
            )


class Logout(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        로그아웃
        POST /api/v1/users/logout/
        """
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()

            response = Response(
                {"message": "Logout Success"}, status=status.HTTP_200_OK
            )
            response.delete_cookie("access")
            response.delete_cookie("refresh")

            return response
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UsersDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_user(self, pk):
        return get_object_or_404(User, pk=pk)

    def get(self, request, pk):
        """
        회원 정보
        GET /api/v1/users/{pk}/
        """
        user = self.get_user(pk=pk)
        request_user = request.user
        if request_user == user or request_user.is_staff:
            serializer = serializers.UsersSerializer(user)

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


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
