from django.forms import ModelForm, widgets
from user.models import Review

class ReviewCreateForm(ModelForm):

    class Meta:
        model = Review
        exclude = ['id', 'user']
        widgets = {'review': widgets.TextInput(attrs={'class': 'form-control'}),
                   }