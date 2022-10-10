from django.db import models

# Create your models here.
class Costumer(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    phonenumber = models.CharField(max_length=12)
    email= models.EmailField()

class reservation(models.Model): 
    date = models.DateField()
    time = models.TimeField()
    number_of_people = models.IntegerField()
    costumer = models.ForeignKey(Costumer, on_delete=models.CASCADE, related_name="costumer")
