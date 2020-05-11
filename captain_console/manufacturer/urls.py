from product import views as product_views
from manufacturer import views as manu_views
from django.urls import path

urlpatterns = [
    path('', manu_views.index, name="manufacturer-index"),
    path('<int:id>', manu_views.get_manufacturer_by_id, name="manufacturer_details"),
    path('consoles/<int:id>', product_views.get_console_by_id, name="console_details"),
    path('games/<int:id>', product_views.get_game_by_id, name="console_details")
]
