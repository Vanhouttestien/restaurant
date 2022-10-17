from django.db import models
from django import forms
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


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

    def __str__(self):
        return f"{self.fname} {self.lname}"


class Reservation(models.Model):
    TIME_CHOICES= [
    ('17:30', '17:30'),
    ('18:00', '18:00'),
    ('18:30', '18:30'),
    ('19:00', '19:00'),
    ('19:30', '19:30'),
    ('20:00', '20:00'),
    ('20:30', '20:30'),
    ('21:00', '21:00'),
    ('21:30', '21:30'),
    ('22:00', '22:00'),
    ]
    
    date = models.DateField()
    number_of_people = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    timeslot = models.CharField(max_length=8, choices=TIME_CHOICES)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,blank=True, null=True
    )
    comments = models.TextField(blank=True, null=True)
    completed = models.BooleanField(blank=True, null=True)
    
    class Meta: 
        get_latest_by = 'date'