from product.models import Product

def items_in_wishlist(request):
  count = Product.objects.filter(user_id=request.user.id).count()
  return {'numberOfItems': count}

def items_in_reviewlist(request):
  count = Product.objects.filter(user_id=request.user.id).count()
  return {'numberOfItems': count}