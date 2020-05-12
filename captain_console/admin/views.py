import json

from django.contrib.auth import login
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from product.models import Product, ProductImage
from templates.admin.forms.login_form import AdminAuthenticationForm


# Create your views here.
from templates.admin.forms.product_form import GameUpdateForm, ConsoleUpdateForm, GameCreateForm


def admin_login(request):
    if request.method == 'POST':
        form = AdminAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('admin_home')
    else:
        form = AdminAuthenticationForm()
    return render(request,'admin/admin_login.html', {
        'form': form
    })

def admin_home(request):
    products = Product.objects.all()
    return render(request, 'admin/index.html', {
        'products': products
    })

def list_products(request, type_id):
    products = Product.objects.filter(type_id=type_id)
    return render(request, 'admin/products.html', {
        'products': products,
        'type_id': type_id
    })

def edit_product(request, id):
    instance = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        if instance.type_id == 1: #games
            form = GameUpdateForm(data=request.POST, instance=instance)
            if form.is_valid():
                product = form.save()
                product_image = ProductImage(image=request.POST['image'], product=product)
                product_image.save()

                return redirect('admin_home')
        elif instance.type_id == 2:
            form = ConsoleUpdateForm(data=request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('admin_home', id=id)
    else:
        if instance.type_id == 1:  # games
            form = GameUpdateForm(instance=instance)
        elif instance.type_id == 2:
            form = ConsoleUpdateForm(instance=instance)
    return render(request, 'admin/edit_product.html', {
        'form': form,
        'id': id
    })

def delete_product(request):
    if request.is_ajax() and request.method == "POST" and request.user.is_authenticated:
        c = json.loads(request.body.decode('utf-8'))
        pid = c["product_id"]
        Product.objects.get(id=pid).delete()
    return JsonResponse({})

def create_game(request):
    if request.method == "POST":
        form = GameCreateForm(data=request.POST)

        if form.is_valid():
            product = form.save()
            product_image = ProductImage(image=request.POST['image'], product=product)
            product_image.save()
            return redirect('admin_home')
    else:
        form = GameCreateForm()
    return render(request, 'admin/create_game.html', {
        'form': form
    })

def single_product(request, id):
    return render(request, 'admin/single_product.html', {
        'product': get_object_or_404(Product, pk=id)
    })


def delete_image(request):
    if request.is_ajax() and request.method == "POST" and request.user.is_authenticated:
        c = json.loads(request.body.decode('utf-8'))
        iid = c["image_id"]
        ProductImage.objects.get(id=iid).delete()
    return JsonResponse({})




