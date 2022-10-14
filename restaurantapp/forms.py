
from django import forms
from .models import Reservation

class DateInput(forms.DateInput):
    input_type='date'

class ReservationForm(forms.ModelForm):
    class Meta: 
        model = Reservation
        fields = '__all__'
        widgets = {
            'date': DateInput()
        }
