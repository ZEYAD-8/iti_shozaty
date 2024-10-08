from django.shortcuts import render, redirect
from . import models
from .forms import Order_Form
from django.contrib.auth.decorators import login_required


def all_shoes(request):
    shoes = models.Shoe.objects.all()
    return render(request, 'all_shoes.html', {'shoes': shoes})

def shoe_details(request, shoe_id):
    shoe = models.Shoe.objects.get(pk=shoe_id)
    return render(request, 'shoe_details.html', {'shoe': shoe})

@login_required()
def order(request, shoe_id):
    shoe = models.Shoe.objects.get(pk=shoe_id)
    if request.method == 'POST':
        form = Order_Form(request.POST, user=request.user)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total = shoe.price
            order.product = shoe
            order.status = 'Pending'
            order.save()
            shoe.stock -= 1
            shoe.save()
            return redirect('profile')  
        else:
            print("Form isn't valid.\nErrors:", form.errors)  
    else:
        form = Order_Form(user=request.user)
    
    return render(request, 'order.html', {'form': form, 'shoe': shoe})
