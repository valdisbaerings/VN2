from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from product.models import Product


class Order(models.Model):
    pass
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    # fullname
    # streetname
    # housenumber
    # city
    # country
    # postalcode
    # date
    # total_price

    #def __unicode__(self):
     #   return "Order id: %s" %(self.id)

class OrderItem(models.Model):
    pass
    #product
    #price
    #count
    #order = models.ForeignKey(Order, on_delete=models.CASCADE)