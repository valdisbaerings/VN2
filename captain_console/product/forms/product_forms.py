from django.forms import widgets, ModelForm
from django import forms

#from console.models import Console
from product.models import Product


class ConsoleCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Product
        exclude = ['id']
        widgets = {'name': widgets.TextInput(attrs={'class': 'form-control'}),
                   'description': widgets.TextInput(attrs={'class': 'form-control'}),
                   'manufacturer': widgets.Select(attrs={'class': 'form-control'}),
                   'price': widgets.NumberInput(attrs={'class': 'form-control'}),

                   }


class ConsoleUpdateForm(ModelForm):
    class Meta:
        model = Product
        exclude = ['id']
        widgets = {'name': widgets.TextInput(attrs={'class': 'form-control'}),
                   'description': widgets.TextInput(attrs={'class': 'form-control'}),
                   'manufacturer': widgets.Select(attrs={'class': 'form-control'}),
                   'price': widgets.NumberInput(attrs={'class': 'form-control'}),
                   }
