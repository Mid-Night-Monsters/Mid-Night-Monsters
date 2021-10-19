from django.db import models
from django.contrib.auth.models import User

from restaurant.models import Restaurant, Product

# Create your models here.
class Consumer(models.Model):
    """
    This class represents the consumer model.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Order(models.Model):
    choices = (
        ('P', 'Pending'),
        ('C', 'Confirmed'),
        ('D', 'Delivered'),
    )
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
    products = models.ManyToManyField(Product)
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=choices, default='P')
    
