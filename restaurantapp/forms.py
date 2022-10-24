from django import forms
from .models import Reservation,ReservationNoUser
from allauth.account.forms import SignupForm

class DateInput(forms.DateInput):
    input_type='date'

class ReservationForm(forms.ModelForm):
    class Meta: 
        model = Reservation
        fields = [ 'timeslot',  'date', 'number_of_people', 'comments']
        widgets = {
            'date': DateInput()
        }

class ReservationNoUserForm(forms.ModelForm):
    class Meta: 
        model = ReservationNoUser
        fields = [ 'fname', 'lname','email','timeslot',  'date', 'number_of_people', 'comments']
        widgets = {
            'date': DateInput()
        }
# class CostumerForm(forms.ModelForm):
#     class Meta:
#         model=Customer
#         fields='__all__'


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