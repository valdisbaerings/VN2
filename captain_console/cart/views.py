from django.shortcuts import render
from django.http import JsonResponse
from .models import Cart
from product.models import Product
import json

def view(request):
    cart = Cart.objects.all()
    context = {"cart": cart}
    template = "cart/index.html"
    return render(request, template, context)


def add_to_cart(request):
    if request.is_ajax() and request.method == "POST" and request.user.is_authenticated:
        print(request.body)
        p = json.loads(request.body.decode('utf-8'))
        pid = p["product_id"]
        product = Product.objects.get(id=pid)
        cart = Cart.objects.filter(product=product, user_id=request.user.id).first()
        if cart is not None:
            cart.quantity += 1
            cart.total += product.price
        else:
            obj = {'total':product.price, 'quantity':1,'product':product,'user_id':request.user.id}
            cart = Cart(**obj)

        cart.save()
        return JsonResponse({'numberOfItems':Cart.objects.filter(user_id=request.user.id).count()})
    return None

def del_to_cart(request):
    Cart.object.get(id=321).delete()
    return JsonResponse({'cart':Cart.object.filter(user=123)})

def number_of_items(request):
    print(request.user.id)
    return JsonResponse({'numberOfItems':10})