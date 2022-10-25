from django.contrib import admin
from .models import  Reservation, ReservationNoUser

@admin.register(Reservation)
class reservationAdmin(admin.ModelAdmin):
     list_display = ('date','timeslot','number_of_people')

@admin.register(ReservationNoUser)
class reservationNoUserAdmin(admin.ModelAdmin):
     list_display = ('date','timeslot','number_of_people')