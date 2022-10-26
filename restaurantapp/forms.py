from django import forms
from .models import Reservation,ReservationNoUser
from allauth.account.forms import SignupForm
import datetime

class DateInput(forms.DateInput):
    input_type='date'

class ReservationForm(forms.ModelForm):
    class Meta: 
        model = Reservation
        fields = [ 'date', 'timeslot',  'number_of_people', 'comments']
        widgets = {
            'date': DateInput()
        }
    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.date.today():
            raise forms.ValidationError("The date cannot be in the past!")
        return date

    def clean_number_of_people(self):
        number_of_people = self.cleaned_data['number_of_people']
        if number_of_people > 15:
            raise forms.ValidationError("For a reservation for more than 15 persons send a mail to il_cucchiaio_d'oro@gmail.com or call +447975777666")
        return number_of_people

class ReservationNoUserForm(forms.ModelForm):
    class Meta:
        model = ReservationNoUser
        fields = [ 'fname', 'lname', 'email', 'timeslot',  'date', 'number_of_people', 'comments']
        widgets = {
            'date': DateInput()
        }

    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.date.today():
            raise forms.ValidationError("The date cannot be in the past!")
        return date

    def clean_number_of_people(self):
        number_of_people = self.cleaned_data['number_of_people']
        if number_of_people > 15:
            raise forms.ValidationError("For a reservation for more than 15 persons send an email to il_cucchiaio_d'oro@gmail.com or call +447975777666")
        return number_of_people

# class from https://www.geeksforgeeks.org/python-extending-and-customizing-django-allauth/

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
 
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user