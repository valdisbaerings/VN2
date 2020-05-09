from django.contrib import admin

# Register your models here.
from order.models import Order


class OrderAdmin(admin.ModelAdmin):
    class Meta:
        model = Order


admin.register(Order, OrderAdmin)
