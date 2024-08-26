from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Trade(models.Model):
    trader = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='trade', null=True)
    trade_type = models.CharField(max_length=4, choices=[('buy', 'Buy'), ('sell', 'Sell')])
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=7,decimal_places=2,default=0.00)
    traded_at = models.DateTimeField(default=datetime.now(),null=True)
    result = models.BooleanField(default=False)
    trading_quantity = models.PositiveIntegerField(default = 0)
    trading_price = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)

