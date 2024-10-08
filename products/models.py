from django.db import models
from categories.models import category
from django.contrib.auth.models import User

class Shoe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='shoe_images/')
    category = models.ForeignKey(category, related_name='shoes', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Orders(models.Model):
    STATUS_CHOICES = [
        ('delivered', 'Delivered'),
        ('in_delivery', 'In Delivery'),
        ('received', 'Received'),
    ]
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='received')
    total = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255)
    address = models.TextField()
    zipcode = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    date = models.DateTimeField(auto_now_add=True)
    order_id = models.CharField(max_length=20)

    def __str__(self):
        return f"Order {self.order_id} by {self.user.username}"
