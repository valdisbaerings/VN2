from product import views as product_views
from manufacturer import views as manu_views
from django.urls import path

urlpatterns = [
    path('', product_views.product_index, name="product-index"),
    path('search_history', product_views.search_index, name="search-index"),
    path('view_search_history', product_views.view_search_index, name="view_search_history"),
    path('consoles', product_views.console_index, name="console-index"),
    path('games', product_views.game_index, name="game-index"),
    path('consoles/<int:id>', product_views.get_console_by_id, name="console_details"),
    path('games/<int:id>', product_views.get_game_by_id, name="game_details"),
    path('<str:order>', product_views.sort_by, name="product-index"),
    path('create_console', product_views.create_console, name="create_console"),
    path('delete_console/<int:id>', product_views.delete_console, name="delete_console"),
    path('update_console/<int:id>', product_views.update_console, name="update_console"),
    path('manufacturers/<int:id>', manu_views.get_manufacturer_by_id, name="product_filter")
]
