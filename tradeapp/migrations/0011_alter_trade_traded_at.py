# Generated by Django 5.1 on 2024-08-26 22:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradeapp', '0010_alter_trade_traded_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='traded_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 27, 7, 33, 3, 370162), null=True),
        ),
    ]
