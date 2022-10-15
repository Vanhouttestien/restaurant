from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('book/', views.book, name='book'),
    path('profile/', views.profile, name='profile'),
    path('order_history/', views.order_history, name='order_history'),
]