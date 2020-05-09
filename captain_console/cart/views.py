from django.shortcuts import render

from .models import Cart

def view(request):
    cart = Cart.objects.all()
    context = {"cart": cart}
    template = "cart/index.html"
    return render(request, template, context)


def add_to_cart(request):
    if request.is_ajax():
        print(request.body)
        # p = json.loads(request.body)
        # p["product_id"]
        return JsonResponse({'bla':'ble'})
        obj = {'total':1, 'quantity':1,'product':1,'user':123}
        cart = Cart(**obj)
        cart.save()
        return JsonResponse({'cart':Cart.object.filter(user=123)})
    return None

def del_to_cart(request):
    Cart.object.get(id=321).delete()
    return JsonResponse({'cart':Cart.object.filter(user=123)})