# Generated by Django 5.1.4 on 2024-12-07 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_orders_car_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Addresses',
        ),
    ]
