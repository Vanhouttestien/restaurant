from django.db import models

from django import forms

TIME_CHOICES= [
    ('17:00', '17:30'),
    ('18:00', '18:30'),
    ('19:00', '19:30'),
    ('20:00', '20:30'),
    ('21:00', '21:30'),
    ]

# Create your models here.
class Costumer(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    phonenumber = models.CharField(max_length=12)
    email= models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)

class reservation(models.Model): 
    date = models.DateField()
    time = models.TimeField()
    number_of_people = models.IntegerField()
    costumer = models.ForeignKey(Costumer, on_delete=models.CASCADE, related_name="costumer")
    created_on = models.DateTimeField(auto_now_add=True)
    timeslot= forms.CharField(label='arrival time', widget=forms.Select(choices=TIME_CHOICES))