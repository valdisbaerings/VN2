from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

from product.forms.product_forms import ConsoleCreateForm, ConsoleUpdateForm
from product.models import Product, ProductImage, SearchHistory, Console
from user.models  import Review, User
from manufacturer.models import Manufacturer
from cart.models import Cart


def sale_index(request):
    products=Product.objects.all()
    return render(request, 'sale/index.html', {
        'products': products
    })


def product_index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        products = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'description': x.description,
            'firstImage': x.productimage_set.first().image,
            'type_id': x.type_id
        }

            for x in Product.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': products})

    if 'product_filter' in request.GET:
        product_filter = request.GET['product_filter']
        consoles = Product.objects.filter(type_id=2, manufacturer_id=product_filter)
        name_list = list(Product.objects.filter(type_id=2, manufacturer_id=product_filter).values_list('name', flat=True))
        con = Console.objects.none()
        for x in range(len(name_list)):
            console_id = Console.objects.filter(name=name_list[x]).values_list('id', flat=True)
            con = console_id.union(console_id, con)
        console_id_list = list(con)
        games = Product.objects.none()
        for x in range(len(con)):
            gam = Product.objects.filter(console_id=console_id_list[x], type_id=1)
            games = games.union(games, gam)
        products = Product.objects.none()
        products = products.union(games, consoles)

        pro = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'description': x.description,
            'firstImage': x.productimage_set.first().image,
            'type_id': x.type_id
        }
            for x in products]

        return JsonResponse({'data': pro})

    if 'product_sorter' in request.GET:
        product_sorter = request.GET['product_sorter']
        products = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'description': x.description,
            'firstImage': x.productimage_set.first().image,
            'type_id': x.type_id
        }
            for x in Product.objects.all().order_by(product_sorter)]
        return JsonResponse({'data': products})

    return render(request, 'product/index.html', context={'products': Product.objects.all().order_by('name'), 'manufacturers': Manufacturer.objects.all()})


def product_index_type(request, type):
    return render(request, 'product/index.html', context={'products': Product.objects.filter(type_id=type).order_by('name')})


def search_index(request):
    if request.method == 'POST':
        print(request)
        form = SearchHistory(name=request.POST['text'])
        form.save()
        return HttpResponse({'name': form})


def view_search_index(request):
    search=SearchHistory.objects.values('name')
    return render(request, 'product/view_search_history.html', {
        'searchhistory': search
    })


def game_index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        products = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'description': x.description,
            'firstImage': x.productimage_set.first().image,
            'type_id': x.type_id
        }

            for x in Product.objects.filter(name__icontains=search_filter, type_id = 1)]
        return JsonResponse({'data': products})

    if 'product_filter' in request.GET:
        product_filter = request.GET['product_filter']
        consoles = Product.objects.filter(type_id=2, manufacturer_id=product_filter)
        name_list = list(Product.objects.filter(type_id=2, manufacturer_id=product_filter).values_list('name', flat=True))
        con = Console.objects.none()
        for x in range(len(name_list)):
            console_id = Console.objects.filter(name=name_list[x]).values_list('id', flat=True)
            con = console_id.union(console_id, con)
        console_id_list = list(con)
        games = Product.objects.none()
        for x in range(len(con)):
            gam = Product.objects.filter(console_id=console_id_list[x], type_id=1)
            games = games.union(games, gam)

        pro = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'description': x.description,
            'firstImage': x.productimage_set.first().image,
            'type_id': x.type_id
        }
            for x in games]

        return JsonResponse({'data': pro})

    if 'product_sorter' in request.GET:
        product_sorter = request.GET['product_sorter']
        products = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'description': x.description,
            'firstImage': x.productimage_set.first().image,
            'type_id': x.type_id
        }
            for x in Product.objects.filter(type_id=1).order_by(product_sorter)]
        return JsonResponse({'data': products})

    return render(request, 'game/index.html', context={'products': Product.objects.filter(type_id=1).order_by('name'),
                                                          'manufacturers': Manufacturer.objects.all()})


def console_index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        products = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'description': x.description,
            'firstImage': x.productimage_set.first().image,
            'type_id': x.type_id
        }

            for x in Product.objects.filter(name__icontains=search_filter, type_id=2)]
        return JsonResponse({'data': products})

    if 'product_filter' in request.GET:
        product_filter = request.GET['product_filter']
        consoles = Product.objects.filter(type_id=2, manufacturer_id=product_filter)

        pro = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'description': x.description,
            'firstImage': x.productimage_set.first().image,
            'type_id': x.type_id
        }
            for x in consoles]

        return JsonResponse({'data': pro})

    if 'product_sorter' in request.GET:
        product_sorter = request.GET['product_sorter']
        products = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'description': x.description,
            'firstImage': x.productimage_set.first().image,
            'type_id': x.type_id
        }
            for x in Product.objects.filter(type_id=2).order_by(product_sorter)]
        return JsonResponse({'data': products})

    return render(request, 'console/index.html', context={'products': Product.objects.filter(type_id=2).order_by('name'),
                                                          'manufacturers': Manufacturer.objects.all()})


def get_console_by_id(request, id):
    return render(request, 'console/console_details.html', {
        'consoles': get_object_or_404(Product, pk=id),'reviews': Review.objects.all(), 'users': User.objects.all()
    })


def get_game_by_id(request, id):
    return render(request, 'game/game_details.html', {
        'games': get_object_or_404(Product, pk=id), 'reviews': Review.objects.all(), 'users': User.objects.all()
    })


def create_console(request):
    if request.method == 'POST':
        form = ConsoleCreateForm(data=request.POST)
        if form.is_valid():
            console = form.save()
            console_image = ProductImage(image=request.POST['image'], console=console)
            console_image.save()
            return redirect('console-index')
    else:
        form = ConsoleCreateForm()
        return render(request, 'console/create_console.html', {
            'form': form
        })


def delete_console(request, id):
    console = get_object_or_404(Product, pk=id)
    console.delete()
    return redirect('console-index')


def update_console(request, id):
    instance = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        form = ConsoleUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('console_details', id=id)
    else:
        form = ConsoleUpdateForm(instance=instance)
        return render(request, 'console/update_console.html', {
            'form': form,
            'id': id
        })
