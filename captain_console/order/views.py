from django.shortcuts import render, redirect
from django.http import JsonResponse
from cart.models import Cart
from product.models import Product
import json
from order.forms.order_form import OrderForm
from .models import OrderItem, Order


def order_items(request):
    context = {}
    template ="order/index.html"
    if request.method == "GET":
        if request.user.is_authenticated:
            if request.session.get("order_id", -1) == -1:
                form = OrderForm()
            else:
                order = Order.objects.get(id = request.session["order_id"])
                form = OrderForm({'fullname': order.fullname, 'streetname': order.streetname, 'housenumber': order.housenumber, 'city': order.city, 'country': order.country, 'postalcode': order.postalcode})

            context["form"] = form
            items = Cart.objects.filter(user_id = request.user.id)
            context["items"] = items
            context["totalPrice"] = sum(item.total for item in items)
            
    elif request.method == "POST" and request.user.is_authenticated:
        form = OrderForm(request.POST)
        if form.is_valid():
            items = Cart.objects.filter(user_id = request.user.id)
            if request.session.get("order_id", -1) == -1:
                order_dict = {
                    'user': request.user,
                    'total_price': sum(item.total for item in items),
                }
                order = Order(**form.cleaned_data, **order_dict)
            else:
                order = Order.objects.get(id = request.session["order_id"], user = request.user)
                order.total_price = sum(item.product.price for item in items)
                order.user = request.user
                order.fullname = form.cleaned_data.get("fullname")
                order.streetname = form.cleaned_data.get("streetname")
                order.housenumber = form.cleaned_data.get("housenumber")
                order.city = form.cleaned_data.get("city")
                order.country = form.cleaned_data.get("country")
                order.postalcode = form.cleaned_data.get("postalcode")

            order.save()
            
            # TODO: hægt að setja þetta í síðasta submit (á summary síðu) - á við um næstu 4 línur
            OrderItem.objects.filter(order=order).delete()

            for item in items:
                OrderItem(product=item.product, price=item.product.price, count=item.quantity, order=order).save()
            
            request.session["order_id"] = order.id

            return redirect('/order/payment')

    return render(request, template, context)


def payment(request):
    context = {}
    template ="order/payment.html"
    if request.method == "GET":
        if request.user.is_authenticated:
            if request.session.get("order_id", -1) == -1:
                form = PaymentForm()
                return redirect('/')
            else:
                payment = Payment.objects.get(id=request.session["order_id"])
                form = OrderForm({'cardholdername': order.cardholdername, 'cardno': order.cardno, 'expdate': order.expdate,
                                  'cvc': order.cvc})

            context["form"] = form

    #order = Order.objects.get(id = request.session["order_id"], user = request.user)
    #payment = Payment.objects.filter(order = order).first()

        # TODO: if payment None, create new payment
    elif request.method == "POST" and request.user.is_authenticated:
        form = PaymentForm(request.POST)
        if form.is_valid():
            if request.session.get("order_id", -1) == -1:
                order = Order(**form.cleaned_data, **order_dict)
            else:
                payment = Payment.objects.filter(order=order).first()
                payment.cardholdername = form.cleaned_data.get("cardholdername")
                payment.cardno = form.cleaned_data.get("cardno")
                payment.expdate = form.cleaned_data.get("expdate")

            payment.save()
            return redirect('/order/review')
        # TODO: update payment
    return render(request, template, context)

"""
- Payment síða
 - GET - gerist þegar notandi fer inn á síðu
    - sýna total price fyrir öll cart items
    - payment formið á að birtast
        - á orderið eitthvað payment
            - ef já nota þær payment upplýsingar í formi
            - annars nýtt tómt form
    - submit takki - vistar form
        - fer á summary síðu
    - tilbaka - fer á order síðu

 - POST - þegar notandi submittar formi
    - er eitthvað skrifað í alla dálka
    - ef hann á payment á þessu order_Id
        - uppfæra upplýsingar
        - annars búa til nýjar payment uppl´syingar fyrir order
    - ef tekst að vista upplýsingar fara á summary/review síðu


- Review
    - GET
        - sækja cart og birta allt í honum
        - sækja order og birta allt
        - sækja payment og birta allt
        <form method="post">
        </form>
        <button type="submit">OK</button>
        - submit takki
    - POST
        - sækja order með request.session[order_id]
        - sækja payment
        - sækja cart
        - vista order item
        - setja completed á order
        request.session["order_id"] = -1

"""
