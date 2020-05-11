from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from manufacturer.models import Manufacturer
#from game.models import Game
#from console.models import Console
from product.models import Product, Console


def index(request):
    context = {'manufacturers': Manufacturer.objects.all()}
    return render(request, 'manufacturer/index.html', context)


def get_manufacturer_by_id(request, id):
    consoles = Product.objects.filter(type_id=2, manufacturer_id=id)
    name_list = list(Product.objects.filter(type_id=2, manufacturer_id=id).values_list('name', flat=True))
    print(name_list)
    con = Console.objects.none()
    for x in range(len(name_list)):
        console_id = Console.objects.filter(name=name_list[x]).values_list('id', flat=True)
        con = console_id.union(console_id, con)
    console_id_list = list(con)
    games = Product.objects.none()
    for x in range(len(con)):
        gam = Product.objects.filter(console_id=console_id_list[x], type_id=1)
        games = games.union(games, gam)
    context = {'consoles': consoles, 'games': games, 'manufacturer': Manufacturer.objects.filter(pk=id)}
    return render(request, 'manufacturer/manufacturer_details.html', context)