
from django import forms
from .models import reservation

class DateInput(forms.DateInput):
    input_type='date'

class reservationForm(forms.ModelForm):
    class Meta: 
        model = reservation
        fields = ['costumer', 'date',]
        widgets = {
            'date': DateInput() 
        }

