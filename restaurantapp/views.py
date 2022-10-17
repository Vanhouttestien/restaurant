from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Reservation
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from . forms import ReservationForm
from django.forms import ModelForm

def index(request):
    return render(request,'index.html')


def profile(request):
    return render(request, 'profile.html')

# class based on https://www.youtube.com/watch?v=llbtoQTt4qw&t=2s
class OrderHistory(LoginRequiredMixin, ListView):
    model = Reservation
    context_object_name='orders'
    template_name = 'restaurantapp/order_history.html'

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['orders'] = context['orders'].filter(user=self.request.user)
        return context

class CreateBooking(ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'


# class based on https://www.youtube.com/watch?v=llbtoQTt4qw&t=2s
class OrderDetail(LoginRequiredMixin, DetailView):
    model = Reservation
    context_object_name = 'order'
    template_name = 'restaurantapp/order_detail.html'

#class based on https://www.youtube.com/watch?v=llbtoQTt4qw&t=2s
class CreateBooking(LoginRequiredMixin, CreateView):
    form_class = ReservationForm
    template_name = 'restaurantapp/book.html'
    success_url = reverse_lazy('order_history')

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(CreateBooking, self).form_valid(form)

# class based on https://www.youtube.com/watch?v=llbtoQTt4qw&t=2s
class UpdateBooking(LoginRequiredMixin, UpdateView):
    model = Reservation
    template_name = 'restaurantapp/book.html'
    fields = ['date', 'timeslot', 'number_of_people', 'comments']
    success_url = reverse_lazy('order_history')

# class based on https://www.youtube.com/watch?v=llbtoQTt4qw&t=2s
class CancelBooking(LoginRequiredMixin, DeleteView):
    model = Reservation
    context_object_name = 'order'
    success_url = reverse_lazy('order_history')

