from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Account(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    carbon_credits = models.PositiveIntegerField(default=500)  # 초기 탄소 배출량
    cash = models.DecimalField(max_digits=10, decimal_places=2, default=5000.00)  # 초기 현금 잔액