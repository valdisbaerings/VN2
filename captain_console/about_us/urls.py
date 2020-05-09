from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="about_us-index"),
]
