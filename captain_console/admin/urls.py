from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_login, name='admin_login'),
    path('home', views.admin_home, name='admin_home'),
    path('logout', LogoutView.as_view(next_page='admin_login'), name='admin_logout'),
    path('edit_product/<int:id>', views.edit_product, name='edit_product'),
    path('delete_product', views.delete_product, name="delete_product"),
    path('create_product', views.create_product, name="create_product"),
    path('products/<int:type_id>', views.list_products, name="list_products"),
    path('single_product/<int:id>', views.single_product, name="single_product"),
    path('delete_image', views.delete_image, name="delete_image")
]