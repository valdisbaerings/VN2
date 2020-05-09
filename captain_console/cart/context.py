from .models import Cart

def items_in_cart(request):
  count = Cart.objects.filter(user_id=request.user.id).count()
  return {'cart': {'numberOfItems': count}}