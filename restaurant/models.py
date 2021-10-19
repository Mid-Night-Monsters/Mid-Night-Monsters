from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name
class Restaurant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    name = models.CharField(max_length=100)

