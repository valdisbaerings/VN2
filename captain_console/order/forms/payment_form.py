from django import forms

class PaymentForm(forms.Form):
    cardholdername = forms.CharField(label='Name of cardholder', max_length=100)
    cardno = forms.CharField(label='Card number', max_length=16, min_length=15, help_text='Must be 16 digits',
                             widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'pattern': '[0-9]+', 'title': 'Enter numbers Only '}))
    expdate = forms.CharField(label='Expiration date', help_text='[MM/YY]')
    cvc = forms.CharField(label='CVC', max_length=4, min_length=3)
