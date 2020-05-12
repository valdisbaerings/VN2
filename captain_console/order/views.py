from django.shortcuts import render, redirect
from django.http import JsonResponse
from cart.models import Cart
from product.models import Product
import json
from order.forms.order_form import OrderForm
from order.forms.payment_form import PaymentForm
from .models import OrderItem, Order, Payment


def order_items(request):
    context = {}
    template ="order/index.html"
    if request.method == "GET":
        if request.user.is_authenticated:
            items = Cart.objects.filter(user_id=request.user.id)
            if len(items)==0:
                return redirect("/")
            if request.session.get("order_id", -1) == -1:
                form = OrderForm()
            else:
                order = Order.objects.get(id=request.session["order_id"])
                form = OrderForm({'fullname': order.fullname, 'streetname': order.streetname, 'housenumber': order.housenumber, 'city': order.city, 'country': order.country, 'postalcode': order.postalcode})

            context["form"] = form
            context["items"] = items
            context["totalPrice"] = sum(item.total for item in items)
            
    elif request.method == "POST" and request.user.is_authenticated:
        form = OrderForm(request.POST)
        if form.is_valid():
            items = Cart.objects.filter(user_id=request.user.id)
            if request.session.get("order_id", -1) == -1:
                order_dict = {
                    'user': request.user,
                    'total_price': sum(item.total for item in items),
                }
                order = Order(**form.cleaned_data, **order_dict)
            else:
                order = Order.objects.get(id=request.session["order_id"], user=request.user)
                order.total_price = sum(item.product.price for item in items)
                order.user = request.user
                order.fullname = form.cleaned_data.get("fullname")
                order.streetname = form.cleaned_data.get("streetname")
                order.housenumber = form.cleaned_data.get("housenumber")
                order.city = form.cleaned_data.get("city")
                order.country = form.cleaned_data.get("country")
                order.postalcode = form.cleaned_data.get("postalcode")

            order.save()
            
            request.session["order_id"] = order.id

            return redirect('/order/payment')

    return render(request, template, context)


def payment(request):
    context = {}
    template ="order/payment.html"
    if request.method == "GET":
        if request.user.is_authenticated:
            items = Cart.objects.filter(user_id=request.user.id)
            if len(items) == 0:
                return redirect("/")
            if request.session.get("order_id", -1) != -1:

                payment = Payment.objects.filter(order_id=request.session["order_id"]).first()
                if payment is None:
                    form = PaymentForm()
                else:
                    form = PaymentForm({'cardholdername': payment.cardholdername, 'cardno': payment.cardno, 'expdate': payment.expdate, 'cvc': payment.cvc})
            else:
                #TODO: Kasta villu því það er ekki til nein pöntun
                return redirect('/')

            context["form"] = form
            items = Cart.objects.filter(user_id=request.user.id)
            context["items"] = items
            context["totalPrice"] = sum(item.total for item in items)
        # TODO: if payment None, create new payment

    elif request.method == "POST" and request.user.is_authenticated:
        form = PaymentForm(request.POST)
        if form.is_valid():
            items = Cart.objects.filter(user_id=request.user.id)
            if request.session.get("order_id", -1) != -1:
                order=Order.objects.get(id=request.session["order_id"], user=request.user)
                payment=Payment.objects.filter(order=order).first()
                if payment is None:
                    payment_dict = {
                        'order': Order.objects.get(id=request.session["order_id"], user=request.user)
                    }
                    payment = Payment(**form.cleaned_data, **payment_dict)
                else:
                    payment.cardholdername = form.cleaned_data.get("cardholdername")
                    payment.cardno = form.cleaned_data.get("cardno")
                    payment.expdate = form.cleaned_data.get("expdate")
                    payment.cvc = form.cleaned_data.get("cvc")
            else:
                pass
                #TODO: kasta villu því þú átt enga pöntun

            payment.save()
            return redirect('/order/review')
        # TODO: update payment
    return render(request, template, context)


def review(request):
    context = {}
    template = "order/review.html"
    if request.method == "GET":
        if request.user.is_authenticated:
            items = Cart.objects.filter(user_id=request.user.id)
            if len(items) == 0:
                return redirect("/")
            if request.session.get("order_id", -1) != -1:
                order = Order.objects.get(id=request.session["order_id"], user=request.user)
                payment = Payment.objects.get(order=order)
                items = Cart.objects.filter(user_id=request.user.id)
                totalPrice = sum(item.total for item in items)
                context={'order': order, 'payment': payment, 'items':items, 'totalPrice': totalPrice}
            else:
                return redirect("/")

    elif request.method == "POST":
        order = Order.objects.get(id=request.session["order_id"], user=request.user)
        items = Cart.objects.filter(user_id=request.user.id)


        for item in items:
            OrderItem(product=item.product, price=item.product.price, count=item.quantity, order=order).save()

        Cart.objects.filter(user_id=request.user.id).delete()
        order.completed = True
        order.save()
        request.session["order_id"] = -1
        return redirect('/order/confirmation')

    return render(request, template, context)


def confirmation(request):
    order = Order.objects.get(id=request.session["order_id"], user=request.user)
    if order.completed == False:
        return redirect("/")
    context = {}
    template = "order/confirmation.html"
    items = Cart.objects.filter(user_id=request.user.id)
    return render(request, template, context)


