from rest_framework import serializers

from accounts.models import Account


class AccountsSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Account
        fields = "__all__"
