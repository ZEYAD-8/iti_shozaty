from django.db import models
from django.contrib.auth.models import User


class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    address = models.TextField()
    joined = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='profile_images/', default='profile_images/default.png')
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

