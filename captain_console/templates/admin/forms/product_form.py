from datetime import datetime

from django.forms import ModelForm, widgets, forms

from product.models import Product

RELEASE_YEAR_CHOICES = []
current_year = int(datetime.now().year)
for year in range(current_year - 1900):
    release_year = 1900 + year
    RELEASE_YEAR_CHOICES.append(release_year)

class ConsoleUpdateForm(ModelForm):
    class Meta:
        model = Product
        exclude = ['id']
        widgets = {'name': widgets.TextInput(attrs={'class': 'form-control'}),
                   'description': widgets.TextInput(attrs={'class': 'form-control'}),
                   'manufacturer': widgets.Select(attrs={'class': 'form-control'}),
                   'price': widgets.NumberInput(attrs={'class': 'form-control'}),
                   'on_sale': widgets.CheckboxInput(attrs={'class': 'checkbox'})
                   }

class GameUpdateForm(ModelForm):
    class Meta:
        model = Product
        exclude = ['id']
        widgets = {'name': widgets.TextInput(attrs={'class': 'form-control'}),
                   'description': widgets.TextInput(attrs={'class': 'form-control'}),
                   'developer': widgets.TextInput(attrs={'class': 'form-control'}),
                   #'release_year': widgets.Select(choices=RELEASE_YEAR_CHOICES),
                   'price': widgets.NumberInput(attrs={'class': 'form-control'}),
                   'on_sale': widgets.CheckboxInput(attrs={'class': 'checkbox'})
                   }
