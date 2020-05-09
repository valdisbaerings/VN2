from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from product.models import Product


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return "Cart id: %s" %(self.id)
