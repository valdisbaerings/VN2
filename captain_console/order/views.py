from django.shortcuts import render
from django.http import JsonResponse
from cart.models import Cart
from product.models import Product
import json

def order_items(request):
    context = {}
    if request.method == "GET":
        if request.user.is_authenticated:
            items = Cart.objects.filter(user_id = request.user.id)
            context["items"] = items
    elif request.method == "POST":
        pass
        # FORM on page sends in fullname, address, etc
        # Fetch all items in cart
        # Copy all items from cart into order item
        # Create and save Order
        order = Order(user=request.user, ....)
        # Create all OrderItems
        items = Cart.objects.filter(user_id = request.user.id)
        for item in items:
            ordItem = OrderItem(product=item.product, price=item.product.price, count=item.quantity, order=order)
            ordItem.save()
    
    template = "order/index.html"
    return render(request, template, context)

