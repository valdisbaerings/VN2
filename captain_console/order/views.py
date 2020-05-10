from django.shortcuts import render
from django.http import JsonResponse
from cart.models import Cart
from product.models import Product
import json
from order.forms.order_form import OrderForm


def order_items(request):
    context = {}
    template ="order/index.html"
    if request.method == "GET":
        if request.user.is_authenticated:
            form = OrderForm()    
            context["form"] = form
            items = Cart.objects.filter(user_id = request.user.id)
            context["items"] = items
            
    elif request.method == "POST" and request.user.is_authenticated:
        form = OrderForm(request.POST)
        if form.is_valid():
            items = Cart.objects.filter(user_id = request.user.id)
            order_dict = {
                'user': request.user,
                'fullname': form.cleaned_data.get("full_name"),
                'streetname': form.cleaned_data.get("street_name"),
                'housenumber': form.cleaned_data.get("house_number"),
                'city': form.cleaned_data.get("city"),
                'country': form.cleaned_data.get("country"),
                'postalcode': form.cleaned_data.get("postal_code"),
                'total_price': sum(item.price for item in items),
            }
            
            order = Order(**order_dict)
            order.save()

            for item in items:
                OrderItem(product=item.product, price=item.product.price, count=item.quantity, order=order).save()

"""
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    price = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    count = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
"""

       #return None
        # FORM on page sends in fullname, address, etc KOMIÐ
        # Fetch all items in cart
        # Copy all items from cart into order item
        # Create and save Order
        #order = Order(user=request.user, ....)
        # Create all OrderItems
        #items = Cart.objects.filter(user_id = request.user.id)
        #for item in items:
         #   ordItem = OrderItem(product=item.product, price=item.product.price, count=item.quantity, order=order)
        #    ordItem.save()

        # template = "order/index.html"
    return render(request, template, context)

