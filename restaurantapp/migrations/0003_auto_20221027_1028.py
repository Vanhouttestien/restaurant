# Generated by Django 3.2.16 on 2022-10-27 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0002_alter_reservationnouser_lname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationnouser',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Email Address'),
        ),
        migrations.AlterField(
            model_name='reservationnouser',
            name='fname',
            field=models.CharField(max_length=50, null=True, verbose_name='First Name'),
        ),
    ]
