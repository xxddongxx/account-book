from rest_framework import serializers

from users.models import User

"""
TODO Token
"""


class UsersRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        username = validated_data.get("username")
        password = validated_data.get("password")
        user = User(username=username)
        user.set_password(password)
        user.save()
        return user


"""
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
"""


# class UsersRegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = [
#             "username",
#             "password",
#         ]


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "name",
            "email",
            "phone",
        ]
