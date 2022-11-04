from django.db import models

from users.models import User


class Account(models.Model):
    amount = models.PositiveIntegerField(verbose_name="금액")
    memo = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="작성자")
    is_delete = models.BooleanField(default=False, verbose_name="삭제여부")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성시간")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정시간")

    def __str__(self):
        return f"{self.amount}: {self.memo[:20]}"
