from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import (
    ListView, DetailView, CreateView,
    UpdateView, DeleteView)
from .models import Reservation, ReservationNoUser
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from . forms import ReservationForm, ReservationNoUserForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from datetime import date
from django.contrib import messages
from django.shortcuts import render


def index(request):
    return render(request, 'restaurantapp/index.html')


def no_user_signin_or_book(request):
    return render(request, 'restaurantapp/no_user_signin_or_book.html')


def about(request):
    return render(request, 'restaurantapp/about.html')


def menu(request):
    return render(request, 'restaurantapp/menu.html')


# class based on https://www.youtube.com/watch?v=llbtoQTt4qw&t=2s
class Orders(LoginRequiredMixin, ListView):
    model = Reservation
    context_object_name = 'orders'
    template_name = 'restaurantapp/orders.html'
    ordering = ['-date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = context['orders'].filter(
            user=self.request.user,
            date__gte=date.today())
        return context


# class based on https://www.youtube.com/watch?v=llbtoQTt4qw&t=2s
class OrderDetail(LoginRequiredMixin, DetailView):
    model = Reservation
    context_object_name = 'order'
    template_name = 'restaurantapp/order_detail.html'


# class based on https://www.youtube.com/watch?v=llbtoQTt4qw&t=2s
class CreateBooking(LoginRequiredMixin, CreateView):
    form_class = ReservationForm
    template_name = 'restaurantapp/book.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Thank you for your booking.')
        return super(CreateBooking, self).form_valid(form)


class CreateBookingNoUser(CreateView):
    form_class = ReservationNoUserForm
    template_name = 'restaurantapp/book_no_user.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Thank you for your booking.')
        return super(CreateBookingNoUser, self).form_valid(form)


# class based on https://www.youtube.com/watch?v=llbtoQTt4qw&t=2s
class UpdateBooking(LoginRequiredMixin, UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'restaurantapp/book.html'
    success_url = reverse_lazy('orders')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Your booking is updated.')
        return super(UpdateBooking, self).form_valid(form)


# class based on https://www.youtube.com/watch?v=llbtoQTt4qw&t=2s
class CancelBooking(LoginRequiredMixin, DeleteView):
    model = Reservation
    context_object_name = 'order'
    success_url = reverse_lazy('orders')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Your booking was canceled.')
        return super(CancelBooking, self).form_valid(form)
