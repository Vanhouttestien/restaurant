from django.contrib import admin
from .models import Costumer, reservation


@admin.register(reservation)
class reservationAdmin(admin.ModelAdmin):
     list_display = ('date', 'time', 'number_of_people')

@admin.register(Costumer)
class costumerAdmin(admin.ModelAdmin):
    list_display = ('lname', 'fname')
    