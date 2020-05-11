from django import forms

class PaymentForm(forms.Form):
    cardholdername = forms.CharField(label='Name of cardholder', max_length=100)
    cardno = forms.IntegerField(label= 'Card number')
    expdate = forms.CharField(label='Expiration date', max_length=5)
    cvc = forms.IntegerField(label= 'CVC')