from django import forms

COUNTRIES = [
  ('iceland', 'Iceland'),
  ('denmark', 'Denmark'),
  ('norway', 'Norway'),
]

class OrderForm(forms.Form):
    full_name = forms.CharField(label='Full name', max_length=100)
    street_name = forms.CharField(label='Street name', max_length=100)
    house_number = forms.CharField(label='House number', max_length=100)
    city = forms.CharField(label='City', max_length=100)
    country = forms.CharField(label='Country', widget=forms.Select(choices=COUNTRIES))
    postal_code = forms.CharField(label='Postal code', max_length=100)