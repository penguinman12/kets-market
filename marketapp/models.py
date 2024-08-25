from django.db import models

# Create your models here.

class Market(models.Model):
    price = models.DecimalField(max_digits=6,decimal_places=2,default=0.00)
    created_at = models.DateField(auto_now_add=True)