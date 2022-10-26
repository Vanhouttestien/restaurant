from . import views
from django.urls import path
from .views import (
    Orders, OrderDetail, CreateBooking,
    UpdateBooking, CancelBooking, CreateBookingNoUser)

urlpatterns = [
    path('', views.index, name='index'),
    path(
        'no_user_signin_or_book/',
        views.no_user_signin_or_book,
        name='no_user_signin_or_book'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('orders/', Orders.as_view(), name='orders'),
    path('order_detail/<int:pk>/', OrderDetail.as_view(), name='order_detail'),
    path('book/', CreateBooking.as_view(), name='book'),
    path('book_no_user/', CreateBookingNoUser.as_view(), name='book_no_user'),
    path(
        'update_booking/<int:pk>/',
        UpdateBooking.as_view(),
        name='update_booking'),
    path(
        'delete_booking/<int:pk>/',
        CancelBooking.as_view(),
        name='delete_booking'),
]
