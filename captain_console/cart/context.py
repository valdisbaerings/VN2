from .models import Cart

def items_in_cart(request):
  cart = Cart.objects.filter(user_id=request.user.id)
  summa = sum( items.quantity for items in cart)
  #count = Cart.objects.filter(user_id=request.user.id).count()
  return {'numberOfItems': '('+str(summa)+')'}