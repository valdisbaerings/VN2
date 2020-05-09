from django.db import models

# Create your models here.
from django.shortcuts import render, get_object_or_404

from manufacturer.models import Manufacturer


class Console(models.Model):
    name = models.CharField(max_length=255)

    # description = models.CharField(max_length=999, blank=True)
    # price = models.FloatField()
    # manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class GameGenre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    price = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    developer = models.CharField(max_length=255, blank=True)
    release_year = models.FloatField()
    console = models.ForeignKey(Console, on_delete=models.CASCADE)
    genre = models.ForeignKey(GameGenre, on_delete=models.CASCADE)
    on_sale=models.BooleanField()

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.CharField(max_length=999)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.image


class SearchHistory(models.Model):
    name=models.CharField(max_length=999)

