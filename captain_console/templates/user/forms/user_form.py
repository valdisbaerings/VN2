from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        #model = CustomUser
        fields = UserCreationForm.Meta.fields + ('first_name','last_name', 'email')
