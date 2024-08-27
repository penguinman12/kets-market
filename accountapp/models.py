from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Account(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    carbon_credits = models.PositiveIntegerField(default=500)  # 초기 탄소 배출량
    cash = models.DecimalField(max_digits=15, decimal_places=2, default=1000000.00)  # 초기 현금 잔액

@receiver(post_save, sender=User)
def create_or_save_user_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)
    instance.account.save()