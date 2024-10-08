from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .models import User_Profile
from .forms import Custom_UserCreationForm, Profile_Update_Form
from products.models import Orders

def profile(request):
    user_profile = User_Profile.objects.get(user=request.user)
    orders = Orders.objects.filter(user=request.user)
    return render(request, 'profiles/profile.html', {'profile': user_profile, 'orders': orders})


def register(request):
    if request.method == 'POST':
        form = Custom_UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user) 
            return redirect('profile') 
    else:
        form = Custom_UserCreationForm()
    return render(request, 'profiles/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'profiles/login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('login')


def update(request):
    user_profile = User_Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = Profile_Update_Form(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = Profile_Update_Form(instance=user_profile, initial={'phone': user_profile.phone, 'address': user_profile.address, 'image': user_profile.image})
    return render(request, 'profiles/edit.html', {'form': form})


