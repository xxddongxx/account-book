from django.contrib.auth.models import AbstractUser, User
from django.db import models


class User(AbstractUser):
    """
    TODO
    email -> password reset 인증에 사용 예정
    """

    username = models.EmailField(max_length=150, unique=True, verbose_name="username")
    first_name = models.CharField(max_length=30, editable=False)
    last_name = models.CharField(max_length=30, editable=False)
    name = models.CharField(max_length=100, verbose_name="name")
    phone = models.CharField(max_length=20, verbose_name="phone")

    def __str__(self):
        return self.name
