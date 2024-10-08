from django.shortcuts import render
from products import models


def home(request):
    shoes = models.Shoe.objects.all()[:10]
    return render(request, 'home.html', {'shoes': shoes})
