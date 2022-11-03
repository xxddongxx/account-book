from rest_framework import serializers

from users.models import User

"""
TODO Token
class UsersRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "password",
        ]

        def save(self, request):
            user = super().save()
            user.username = self.validated_data["username"]
            user.set_password(self.validated_data["password"])
            user.save()
            return user

        def validate(self, data):
            username = data.get("username", None)
            if User.objects.filter(username=username).exists():
                raise serializers.ValidationError("user already exists")
            return data


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
"""

class UsersRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password',]

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
