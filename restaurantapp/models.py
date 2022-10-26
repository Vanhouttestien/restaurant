from django.db import models
from django import forms
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ReservationNoUser(models.Model):
    '''reservation model for users that are not logedin'''
    TIME_CHOICES = [
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

    fname = models.CharField(
        "First Name",
        max_length=50,
        blank=True,
        null=True)
    lname = models.CharField("Last Name", max_length=50, blank=True, null=True)
    email = models.EmailField("Email Address", blank=True, null=True)
    date = models.DateField("Date")
    number_of_people = models.IntegerField("Number of Guests")
    created_on = models.DateTimeField(auto_now_add=True)
    timeslot = models.CharField("Time", max_length=8, choices=TIME_CHOICES)
    comments = models.TextField(
        "Anything else? (Allergies, Special Dietary Wishes,...)",
        blank=True,
        null=True)

    class Meta:
        get_latest_by = 'date'


class Reservation(models.Model):
    '''reservation model for users that are logedin'''
    TIME_CHOICES = [
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
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True)
    date = models.DateField("Date")
    number_of_people = models.IntegerField("Number of Guests")
    created_on = models.DateTimeField(auto_now_add=True)
    timeslot = models.CharField("Time", max_length=8, choices=TIME_CHOICES)
    comments = models.TextField(
        "Anything else? (Allergies, Special Dietary Wishes,...)",
        blank=True,
        null=True)

    class Meta:
        get_latest_by = 'date'
