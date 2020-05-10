import order
from . import views
from django.urls import path

urlpatterns = [
    path('', order.views.order_items, name="order-index"),
    #path('payment', order.views.payment, name="order-index"),
]