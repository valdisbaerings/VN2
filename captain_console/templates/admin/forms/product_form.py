from datetime import datetime

from django import forms
from django.db import models
from django.forms import ModelForm, widgets

from product.models import Product, Console

RELEASE_YEAR_CHOICES = []
current_year = int(datetime.now().year)
for year in range(current_year - 1900):
    my_year = 1900 + year
    RELEASE_YEAR_CHOICES.append(my_year)


class ConsoleUpdateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Product
        exclude = ['id', 'developer', 'release_year', 'console', 'genre', 'type']
        widgets = {'name': widgets.TextInput(attrs={'class': 'form-control'}),
                   'description': widgets.TextInput(attrs={'class': 'form-control', 'size': '40'}),
                   'manufacturer': widgets.Select(attrs={'class': 'form-control'}),
                   'price': widgets.NumberInput(attrs={'class': 'form-control'}),
                   'on_sale': widgets.CheckboxInput(attrs={'class': 'checkbox'})
                   }


class GameUpdateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Product
        exclude = ['id', 'manufacturer', 'type']
        widgets = {'name': widgets.TextInput(attrs={'class': 'form-control'}),
                   'description': widgets.TextInput(attrs={'class': 'form-control'}),
                   'developer': widgets.TextInput(attrs={'class': 'form-control'}),
                   # 'release_year': widgets.Select(choices=RELEASE_YEAR_CHOICES),
                   'price': widgets.NumberInput(attrs={'class': 'form-control'}),
                   'on_sale': widgets.CheckboxInput(attrs={'class': 'checkbox'})
                   }


class ConsoleCreateForm(ModelForm):
    image = forms.CharField(required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    manufacturer = forms.CharField(help_text='[Type: NA]', widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    on_sale = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}))
    developer = forms.CharField(help_text='[Type: NA]', widget=forms.Select(attrs={'class': 'form-control'}))
    release_year = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Product
        exclude = ['id']
        widgets = {
            'console': widgets.Select(attrs={'class': 'form-control'}),
            'genre': widgets.Select(attrs={'class': 'form-control'}),
            'type': widgets.Select(attrs={'class': 'form-control'})
        }

    # Product.developer = 'N/A'

class GameCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Product
        exclude = ['id', 'developer', 'manufacturer']
        widgets = {'name': widgets.TextInput(attrs={'class': 'form-control'}),
                   'type': widgets.Select(attrs={'class': 'form-control'}),
                   'description': widgets.TextInput(attrs={'class': 'form-control'}),
                   'developer': widgets.TextInput(attrs={'class': 'form-control'}),
                   'manufacturer': widgets.Select(attrs={'class': 'form-control'}),
                   'release_year': widgets.NumberInput(attrs={'class': 'form-control'}),
                   'price': widgets.NumberInput(attrs={'class': 'form-control'}),
                   'on_sale': widgets.CheckboxInput(attrs={'class': 'checkbox'})
                   }


class ConsoleForm(ModelForm):

    class Meta:
        model = Console
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
        }
