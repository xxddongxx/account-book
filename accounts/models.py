from django.db import models

class Account(models.Model):
    amount = models.PositiveIntegerField(verbose_name="금액")
    memo = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성시간")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정시간")

    def __str__(self):
        return f'{self.amount}: {self.memo[:20]}'
