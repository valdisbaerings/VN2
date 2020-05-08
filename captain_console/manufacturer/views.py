from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse

# Create your views here.
from manufacturer.models import Manufacturer
#from game.models import Game
#from console.models import Console
from product.models import Product


def index(request):
    context = {'manufacturers': Manufacturer.objects.all()}
    return render(request, 'manufacturer/index.html', context)


def get_manufacturer_by_id(request, id):
    consoles = Product.objects.filter(type_id=2, manufacturer_id=id)
    id_list = list(Product.objects.filter(type_id=2, manufacturer_id=id).values_list('id', flat=True))
    games = Product.objects.none()
    for x in range(len(id_list)):
        gam = Product.objects.filter(console_id=id_list[x])
        games = games.union(games, gam)
    context = {'consoles': consoles, 'games': games, 'manufacturer': Manufacturer.objects.filter(pk=id)}
    return render(request, 'manufacturer/manufacturer_details.html', context)
