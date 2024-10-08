from django.shortcuts import render
from django.db.models import Count
from products.models import Shoe
from . import models 

def all_categories(request):
    category_counts = models.category.objects.annotate(num_shoes=Count('shoe')).values('name', 'num_shoes')
    category_counts = list(category_counts)
    all = models.category.objects.all()

    category_objects = {}
    for category_count in category_counts:
        for category in all:
            if category_count['name'] == category.name:
                category_objects[category] = category_count['num_shoes']
    return render(request, 'all_categories.html', {'categories': category_objects})

def category_shoes(request, category_id):
    shoes = Shoe.objects.filter(category=category_id)
    category_name = models.category.objects.get(pk=category_id).name
    return render(request, 'category_shoes.html', {'shoes': shoes, 'category_name': category_name})
