from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
#class CustomUser(User):
    #fields = User.fields + ('first_name', 'last_name', 'email')
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=9999, default='https://img.icons8.com/pastel-glyph/512/000000/user-male--v1.png')

    def create_profile(sender, **kwargs):
        user = kwargs["instance"]
        if kwargs["created"]:
            user_profile = Profile(user=user)
            user_profile.save()

    post_save.connect(create_profile, sender=User)





