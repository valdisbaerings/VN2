from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Cart
from product.models import Product
import json


def view(request):
    context = {'items': []}
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user_id=request.user.id)
        context["items"] = cart
        total_price = sum(c.total for c in cart)
        context["totalPrice"] = total_price
        template = "cart/index.html"
    return render(request, template, context)


def add_to_cart(request):
    if request.is_ajax() and request.method == "POST" and request.user.is_authenticated:
        p = json.loads(request.body.decode('utf-8'))
        pid = p["product_id"]
        product = Product.objects.get(id=pid)
        cart = Cart.objects.filter(product=product, user_id=request.user.id).first()
        if cart is not None:
            cart.quantity += 1
            cart.total += product.price
        else:
            obj = {'total': product.price, 'quantity': 1, 'product': product, 'user_id': request.user.id}
            cart = Cart(**obj)

        cart.save()
        return JsonResponse({'numberOfItems': Cart.objects.filter(user_id=request.user.id).count()})
    elif request.user.is_authenticated == False:
        return HttpResponse(status=404)
    return None


def del_from_cart(request):
    if request.is_ajax() and request.method == "POST" and request.user.is_authenticated:
        c = json.loads(request.body.decode('utf-8'))
        cid = c["cart_id"]
        Cart.objects.get(id=cid).delete()
    return JsonResponse({})


def number_of_items(request):
    print(request.user.id)
    return JsonResponse({'numberOfItems': 10})
