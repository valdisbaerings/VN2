from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

from product.forms.product_forms import ConsoleCreateForm, ConsoleUpdateForm
from product.models import Product, ProductImage, SearchHistory


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
    return render(request, 'product/index.html', context={'products': Product.objects.all().order_by('name')})


def search_history(request):
    print("HAAA")
    search="BLAA"
    if request.method == 'POST':
        search = SearchHistory(name=request.POST(search))
        search.save()
    return redirect('product-index')


def game_index(request):
    return render(request, 'game/index.html', {'products': Product.objects.all()})


def console_index(request):
    return render(request, 'console/index.html', {'products': Product.objects.all()})


def get_console_by_id(request, id):
    return render(request, 'console/console_details.html', {
        'consoles': get_object_or_404(Product, pk=id)
    })


def get_game_by_id(request, id):
    return render(request, 'game/game_details.html', {
        'games': get_object_or_404(Product, pk=id)
    })


def create_product(request):
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


def delete_product(request, id):
    console = get_object_or_404(Product, pk=id)
    console.delete()
    return redirect('console-index')


def update_product(request, id):
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


def sort_by(request, filter):
    return render(request, 'product/index.html', context={'products': Product.objects.all().order_by(filter)})