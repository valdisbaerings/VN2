import json

from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from product.models import Product, ProductImage, Console
from templates.admin.forms.login_form import AdminAuthenticationForm
from templates.admin.forms.product_form import ProductUpdateForm, ProductCreateForm

user_login_required = user_passes_test(lambda user: user.is_superuser, login_url='/admin')
def superuser_required(view_func):
    decorated_view_func = login_required(user_login_required(view_func), login_url='/admin')
    return decorated_view_func

# Create your views here.

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

@superuser_required
def admin_home(request):
    products = Product.objects.all()
    return render(request, 'admin/index.html', {
        'products': products
    })

@superuser_required
def list_products(request, type_id):
    products = Product.objects.filter(type_id=type_id)
    return render(request, 'admin/products.html', {
        'products': products.order_by('name'),
        'type_id': type_id
    })

@superuser_required
def edit_product(request, id):
    instance = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        form = ProductUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            product = form.save()
            product_image = ProductImage(image=request.POST['image'], product=product)
            if product_image.image is not '':
                product_image.save()
    else:
        form = ProductUpdateForm(instance=instance)
    return render(request, 'admin/edit_product.html', {
        'form': form,
        'id': id
    })

@superuser_required
def delete_product(request):
    if request.is_ajax() and request.method == "POST" and request.user.is_authenticated:
        c = json.loads(request.body.decode('utf-8'))
        pid = c["product_id"]
        product = Product.objects.get(id=pid)
        if product.type_id == 2:
            Console.objects.get(name=product.name).delete()
        Product.objects.get(id=pid).delete()
    return JsonResponse({})

@superuser_required
def create_game(request):
    if request.method == "POST":
        form = ProductCreateForm(data=request.POST)
        if form.is_valid():
            product = form.save()
            product_image = ProductImage(image=request.POST['image'], product=product)
            product_image.save()
            return redirect('products/'+str(product.type_id))
    else:
        form = ProductCreateForm()
    return render(request, 'admin/create_game.html', {
        'form': form
    })

@superuser_required
def create_console(request):
    if request.method == "POST":
        form = ProductCreateForm(data=request.POST)
        print(form['manufacturer'])
        if form.is_valid():
            product = form.save()
            product_image = ProductImage(image=request.POST['image'], product=product)
            product_image.save()
            return redirect('products/'+str(product.type_id))
    else:
        form = ProductCreateForm()
    return render(request, 'admin/create_console.html', {
        'form': form
    })


@superuser_required
def single_product(request, id):
    return render(request, 'admin/single_product.html', {
        'product': get_object_or_404(Product, pk=id)
    })

@superuser_required
def delete_image(request):
    if request.is_ajax() and request.method == "POST" and request.user.is_authenticated:
        c = json.loads(request.body.decode('utf-8'))
        iid = c["image_id"]
        ProductImage.objects.get(id=iid).delete()
    return JsonResponse({})




