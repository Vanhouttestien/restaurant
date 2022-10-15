from django.db import models
from django import forms
from django.conf import settings
from django.db import models


# Create your models here.
class Costumer(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,blank=True, null=True
    )
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    phonenumber = models.CharField(max_length=12)
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)


class Reservation(models.Model):
    TIME_CHOICES= [
    (1, '17:30'),
    (2, '18:00'),
    (3, '18:30'),
    (4, '19:00'),
    (5, '19:30'),
    (6, '20:00'),
    (7, '20:30'),
    (8, '21:00'),
    (9, '21:30'),
    (10, '22:00'),
    ]
    date = models.DateField()
    number_of_people = models.IntegerField()
    costumer = models.ForeignKey(Costumer, on_delete=models.CASCADE, related_name="costumer")
    created_on = models.DateTimeField(auto_now_add=True)
    timeslot = models.IntegerField(choices=TIME_CHOICES)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,blank=True, null=True
    )
    

