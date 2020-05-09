from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, widgets
from user.models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = [ 'id', 'user' ]
        widgets = {
            'profile_image': widgets.TextInput(attrs={ 'class': 'form-control' })
        }

    #def save(self):
        #self.user_id = ModelForm.id

        #model = User
        #exclude = ['id', 'user']
        #widgets = {
            #'first_name': widgets.TextInput(attrs=)
        #}
