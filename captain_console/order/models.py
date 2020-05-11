from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from product.models import Product
from user.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255)
    streetname = models.CharField(max_length=255)
    housenumber = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    postalcode = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    total_price = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    completed = models.BooleanField(default=False)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    price = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    count = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)


class Payment(models.Model):
    cardholdername = models.CharField(max_length=100)
    cardno = models.DecimalField(max_digits=16, decimal_places=10)
    expdate = models.CharField(max_length=5)
    cvc = models.DecimalField(max_digits=3, decimal_places=2)