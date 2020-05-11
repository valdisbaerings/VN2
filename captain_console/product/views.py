from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

from product.forms.product_forms import ConsoleCreateForm, ConsoleUpdateForm
from product.models import Product, ProductImage, SearchHistory, ProductForm, Manufacturer
from user.models  import Review, User
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
            'description': x.description,
            'firstImage': x.productimage_set.first().image
        }

            for x in Product.objects.filter(name__icontains=search_filter)]
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
    return render(request, 'game/index.html', {'products': Product.objects.all()})


def console_index(request):
    return render(request, 'console/index.html', {'products': Product.objects.all()})


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


def sort_by(request, order):
    if order == 'reverse':
        return render(request, 'product/index.html', context={'products': Product.objects.all().order_by('-price')})
    else:
        return render(request, 'product/index.html', context={'products': Product.objects.all().order_by(order)})


def product_filter(request, manu_name):
    qs = Product.objects.all()
    manufacturer = Manufacturer.objects.all()
    qs = qs.filter(manu_name=manufacturer)
    return render(request, 'product/index.html', context={'products': qs, 'manufacturers': manufacturer})


