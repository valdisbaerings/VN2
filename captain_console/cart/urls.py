import cart
from . import views
from django.urls import path

urlpatterns = [
    path('', cart.views.view, name="cart-index"),
]