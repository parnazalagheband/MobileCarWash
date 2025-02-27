# Generated by Django 5.0.4 on 2024-08-22 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_customeruser'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeruser',
            name='gender',
            field=models.CharField(blank=True, choices=[('female', 'female'), ('male', 'male')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='workeruser',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
