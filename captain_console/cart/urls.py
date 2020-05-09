import cart
from . import views
from django.urls import path

urlpatterns = [
    path('', cart.views.view, name="cart-index"),
    path('addToCart', cart.views.add_to_cart, name="cart-add"),
    path('numberOfItems', cart.views.number_of_items, name="cart-count"),
    path('deleteFromCart', cart.views.del_from_cart, name="cart-del")
]