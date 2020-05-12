from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404

from product.models import Product
from templates.admin.forms.login_form import AdminAuthenticationForm


# Create your views here.
from templates.admin.forms.product_form import GameUpdateForm, ConsoleUpdateForm


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

def edit_product(request, id):
    instance = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        if instance.type_id == 1: #games
            form = GameUpdateForm(data=request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('console_details', id=id)
        elif instance.type_id == 2:
            form = ConsoleUpdateForm(data=request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('console_details', id=id)
    else:
        if instance.type_id == 1:  # games
            form = GameUpdateForm(instance=instance)
            print('hello')
        elif instance.type_id == 2:
            form = ConsoleUpdateForm(instance=instance)
    return render(request, 'admin/edit_product.html', {
        'form': form,
        'id': id
    })




