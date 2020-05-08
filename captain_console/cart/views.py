from django.shortcuts import render

from .models import Cart

def view(request):
    cart = Cart.objects.all()
    context = {"cart": cart}
    template = "cart/index.html"
    return render(request, template, context)
