from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="manufacturer-index"),
    path('<int:id>', views.get_manufacturer_by_id, name="manufacturer_details")
]
