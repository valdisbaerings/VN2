from datetime import datetime

from django import forms
from django.db import models
from django.forms import ModelForm, widgets

from product.models import Product

RELEASE_YEAR_CHOICES = []
current_year = int(datetime.now().year)
for year in range(current_year - 1900):
    my_year = 1900 + year
    release_year_str = str(my_year)
    RELEASE_YEAR_CHOICES.append(release_year_str)

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
        exclude = ['id', 'manufacturer','type']
        widgets = {'name': widgets.TextInput(attrs={'class': 'form-control'}),
                   'description': widgets.TextInput(attrs={'class': 'form-control'}),
                   'developer': widgets.TextInput(attrs={'class': 'form-control'}),
                   #'release_year': widgets.Select(choices=RELEASE_YEAR_CHOICES),
                   'price': widgets.NumberInput(attrs={'class': 'form-control'}),
                   'on_sale': widgets.CheckboxInput(attrs={'class': 'checkbox'})
                   }

class ConsoleCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Product
        #Product.developer = 'N/A'
        exclude = ['id', 'developer', 'release_year', 'console', 'genre', 'type']
        widgets = {'name': widgets.TextInput(attrs={'class': 'form-control'}),
                   'description': widgets.TextInput(attrs={'class': 'form-control', 'size': '40'}),
                   'manufacturer': widgets.Select(attrs={'class': 'form-control'}),
                   'price': widgets.NumberInput(attrs={'class': 'form-control'}),
                   'on_sale': widgets.CheckboxInput(attrs={'class': 'checkbox'})
                   }

class GameCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Product
        exclude = ['id', 'type']
        widgets = {'name': widgets.TextInput(attrs={'class': 'form-control'}),
                   'description': widgets.TextInput(attrs={'class': 'form-control'}),
                   'developer': widgets.TextInput(attrs={'class': 'form-control'}),
                   'manufacturer': widgets.Select(attrs={'class': 'form-control'}),
                   # 'release_year': widgets.Select(choices=RELEASE_YEAR_CHOICES),
                   'price': widgets.NumberInput(attrs={'class': 'form-control'}),
                   'on_sale': widgets.CheckboxInput(attrs={'class': 'checkbox'})
                   }