from django import forms

COUNTRIES = [
  ('iceland', 'Iceland'),
  ('denmark', 'Denmark'),
  ('norway', 'Norway'),
]

class OrderForm(forms.Form):
    fullname = forms.CharField(label='Full name', max_length=100)
    streetname = forms.CharField(label='Street name', max_length=100)
    housenumber = forms.CharField(label='House number', max_length=10)
    city = forms.CharField(label='City', max_length=100)
    country = forms.CharField(label='Country', widget=forms.Select(choices=COUNTRIES))
    postalcode = forms.CharField(label='Postal code', max_length=10)