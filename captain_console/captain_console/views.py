from django.shortcuts import render
from django.http import HttpResponse
from product.models import Product

# Create your views here.
def index(request):
    return render(request, 'homepage/index.html',context={'products': Product.objects.all()} )