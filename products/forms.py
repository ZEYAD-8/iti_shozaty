
from django import forms
from .models import Orders
from profiles.models import User_Profile




class Order_Form(forms.ModelForm):

    class Meta:
        model = Orders
        fields = ['email', 'address', 'zipcode', 'phone', 'total']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 4}),
        }
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)


        if user and user.is_authenticated:
            user_profile = User_Profile.objects.get(user=user)
            self.fields['email'].initial = user.email
            self.fields['phone'].initial = user_profile.phone
            self.fields['address'].initial = user_profile.address
