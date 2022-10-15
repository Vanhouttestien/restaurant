from django.contrib import admin
from .models import Costumer, Reservation


@admin.register(Reservation)
class reservationAdmin(admin.ModelAdmin):
     list_display = ('date','timeslot','number_of_people')

@admin.register(Costumer)
class costumerAdmin(admin.ModelAdmin):
    list_display = ('lname', 'fname')