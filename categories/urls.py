from .views import *
from django.urls import path

urlpatterns = [
    path('', all_categories, name='all_categories'),
    path('<int:category_id>/', category_shoes, name='category_shoes'),
]
