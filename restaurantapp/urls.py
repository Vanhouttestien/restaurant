from . import views
from django.urls import path
from .views import OrderHistory, OrderDetail, CreateBooking, UpdateBooking, CancelBooking
# CostumLoginView

urlpatterns = [
    # path('login/',CostumLoginView.as_view(), name='login'),
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('order_history/', OrderHistory.as_view(), name='order_history'),
    path('order_detail/<int:pk>/', OrderDetail.as_view(), name='order_detail'),
    path('book/', CreateBooking.as_view(),name='book'),
    path('update_booking/<int:pk>/', UpdateBooking.as_view(), name='update_booking'),
    path('delete_booking/<int:pk>/', CancelBooking.as_view(), name='delete_booking'),
]