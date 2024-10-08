
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_shoes, name='all_shoes'),
    path('<int:shoe_id>/', views.shoe_details, name='shoe_details'),
    path('<int:shoe_id>/order/', views.order, name='order'),
]
