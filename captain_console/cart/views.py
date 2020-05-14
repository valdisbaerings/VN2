from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.db.models import Count
from .models import Cart, Product
from product.models import Product
from decimal import Decimal
import json

@login_required
def view(request):
    context = {'items': []}
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user_id=request.user.id)
        items = Cart.objects.filter(user_id=request.user.id)
        context["items"] = cart

        DiscountPrice = 0
        totalPrice = 0
        for item in items:
            if item.product.on_sale == True:
                DiscountPrice += item.total * Decimal(0.2)
                totalPrice += item.total * Decimal(0.8)
            else:
                totalPrice += item.total
        DiscountPrice = round(DiscountPrice, 2)
        totalPrice = round(totalPrice, 2)

        total_price = sum(c.total for c in cart)


        #DiscountPrice = 5
        context["totalPrice"] = totalPrice
        context["DiscountPrice"] = DiscountPrice
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
       # cart = Cart.objects.filter(user_id=request.user.id)
        cart = Cart.objects.filter(user_id=request.user.id)
        summa = sum(items.quantity for items in cart)
        #Cart.objects.filter(user_id=request.user.id).count()
        return JsonResponse({'numberOfItems': '(' + str(summa) +')'})
    elif request.user.is_authenticated == False:
        return HttpResponse(status=404)
    return None

@login_required
def del_from_cart(request):
    if request.is_ajax() and request.method == "POST" and request.user.is_authenticated:
        c = json.loads(request.body.decode('utf-8'))
        cid = c["cart_id"]
        Cart.objects.get(id=cid).delete()
    return JsonResponse({})


def number_of_items(request):
    cart = Cart.objects.filter(user_id=request.user.id)
    return JsonResponse({'numberOfItems': 10})
