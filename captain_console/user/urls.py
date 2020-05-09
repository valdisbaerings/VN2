from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile', views.profile, name='profile'),
    path('profile_picture', views.profile_picture, name='profile_picture')
    #path('update_profile', views.update_profile, name='update_profile')
    #path('view_profile', views.view_profile, name='view_profile')
]