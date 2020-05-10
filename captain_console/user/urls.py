from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile', views.profile, name='profile'),
    path('profile_picture', views.profile_picture, name='profile_picture'),
    path('update_profile', views.update_profile, name='update_profile'),
    path('change_password', views.change_password, name='change_password'),
    path('addToWishlist', views.add_to_wishlist, name="add-to-wishlist"),
    path('viewWishlist', views.view_wishlist, name="view-wishlist"),
    path('deleteFromWishlist', views.del_from_wishlist, name="wishlist-del"),
    path('review/<int:id>', views.review_index, name="review_index"),
    path('review/<int:id>/add_review', views.add_review, name="add_review"),
    path('review/get_my_reviews', views.get_my_reviews, name="get_my_reviews"),

]
