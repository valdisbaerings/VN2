from . import views
from django.urls import path

urlpatterns = [
    path('', views.product_index, name="product-index"),
    path('consoles', views.console_index, name="console-index"),
    path('games', views.game_index, name="game-index"),
    path('consoles/<int:id>', views.get_console_by_id, name="console_details"),
    path('games/<int:id>', views.get_game_by_id, name="game_details"),
    path('<str:filter>', views.sort_by, name="product-index"),
    path('create_product', views.create_product, name="create_product"),
    path('delete_product/<int:id>', views.delete_product, name="delete_product"),
    path('update_product/<int:id>', views.update_product, name="update_product")
]