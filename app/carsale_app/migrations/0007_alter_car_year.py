# Generated by Django 4.2.3 on 2023-07-11 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carsale_app', '0006_billinginfo_account_is_active_account_is_staff_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.PositiveIntegerField(default=''),
        ),
    ]
