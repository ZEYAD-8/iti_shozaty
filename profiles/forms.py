
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models

class Custom_UserCreationForm(UserCreationForm):
   
    username = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=True)
    address = forms.CharField(widget=forms.Textarea, required=False)
    image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
       
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

      
        if commit:
            models.User_Profile.objects.create(
                user=user,
                phone=self.cleaned_data['phone'],
                address=self.cleaned_data['address'],
                image=self.cleaned_data.get('image', 'profile_images/default.png')
            )

        return user




class Profile_Update_Form(forms.ModelForm):
    class Meta:
        model = models.User_Profile
        fields = ['phone', 'address', 'image']
