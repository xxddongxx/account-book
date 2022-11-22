from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
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
            refresh_token = str(token)
            access_token = str(token.access_token)
            response = Response(
                {
                    "user": serializer.data,
                    "message": "login success",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )
            return response
        else:
            return Response(
                {"message": "로그인에 실패하였습니다."}, status=status.HTTP_400_BAD_REQUEST
            )


class Logout(APIView):
    def post(self, request):
        """
        로그아웃
        POST /api/v1/users/logout/
        """
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UsersDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        """
        회원 정보
        GET /api/v1/users/{pk}/
        """
        user = User.objects.get(pk=pk)
        request_user = request.user
        if request_user == user or request.user.is_staff:
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
