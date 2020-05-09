from . import views
from django.urls import path

urlpatterns = [
    path('', views.product_index, name="product-index"),
    path('search_history', views.search_index, name="search-index"),
    path('view_search_history', views.view_search_index, name="view_search_history"),
    path('consoles', views.console_index, name="console-index"),
    path('games', views.game_index, name="game-index"),
    path('consoles/<int:id>', views.get_console_by_id, name="console_details"),
    path('games/<int:id>', views.get_game_by_id, name="game_details"),
    path('<str:filter>', views.sort_by, name="product-index"),
    path('create_console', views.create_console, name="create_console"),
    path('delete_console/<int:id>', views.delete_console, name="delete_console"),
    path('update_console/<int:id>', views.update_console, name="update_console")
]
