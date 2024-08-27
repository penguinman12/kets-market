# Generated by Django 5.1 on 2024-08-27 23:14

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradeapp', '0016_alter_trade_traded_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='traded_at',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
