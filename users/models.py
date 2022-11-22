from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):
    """
    Custom User Manager
    """

    def create_user(self, email, username=None, password=None):
        if not email:
            raise ValueError("이메일은 필수 항목입니다.")

        email = self.normalize_email(email)

        user = self.model(email=email, username=username)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username=None, password=None):
        user = self.create_user(email, username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    email = models.EmailField(max_length=120, unique=True, verbose_name="이메일")
    username = models.EmailField(max_length=150, verbose_name="유저명")
    first_name = models.CharField(max_length=30, editable=False)
    last_name = models.CharField(max_length=30, editable=False)
    phone = models.CharField(max_length=20, verbose_name="phone")

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username
