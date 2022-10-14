from django.shortcuts import render
from .models import reservation, Costumer
from .forms import reservationForm


# Create your views here.

def index(request):
    return render(request,'index.html')

def book(request):
    form = reservationForm()
    context = {
        'form': form
        }
    return render(request, 'book.html', context)

