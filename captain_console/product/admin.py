from django.contrib import admin
from django.contrib.auth.models import Group, User
from product.models import Console, Product, Type

# Register your models here.

admin.site.site_header = "Captain Console Admin Site"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'console_id', 'type_id')
    list_filter = ('type_id',)

admin.site.register(Product, ProductAdmin)
admin.site.unregister(Group)
