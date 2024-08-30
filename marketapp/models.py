from django.db import models

# Create your models here.

class Market(models.Model):
    price = models.DecimalField(max_digits=8,decimal_places=2,default=0.00)
    market_date = models.DateField(null=True)