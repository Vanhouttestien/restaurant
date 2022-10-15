from django.shortcuts import render
from .models import Reservation, Costumer
from .forms import ReservationForm


# Create your views here.

def index(request):
    return render(request,'index.html')

def book(request):
    form = ReservationForm()
    context = {
        'form': form
        }
    return render(request, 'book.html', context)

def profile(request):
    return render(request, 'profile.html')


def order_history(request):
    return render(request, 'order_history.html')    
