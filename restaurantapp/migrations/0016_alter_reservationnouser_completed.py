# Generated by Django 3.2.16 on 2022-10-19 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0015_reservationnouser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationnouser',
            name='completed',
            field=models.BooleanField(null=True),
        ),
    ]
