from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
#class CustomUser(User):
    #fields = User.fields + ('first_name', 'last_name', 'email')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=9999)






