# Generated by Django 5.1 on 2024-08-25 17:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trade_type', models.CharField(choices=[('buy', 'Buy'), ('sell', 'Sell')], max_length=4)),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('traded_at', models.DateField(auto_now_add=True, null=True)),
                ('result', models.BooleanField(default=False)),
                ('trader', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trade', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
