# Generated by Django 3.2.16 on 2022-10-15 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0002_costumer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='timeslot',
            field=models.IntegerField(choices=[(1, '17:30'), (2, '18:00'), (3, '18:30'), (4, '19:00'), (5, '19:30'), (6, '20:00'), (7, '20:30'), (8, '21:00'), (9, '21:30'), (10, '22:00')]),
        ),
    ]