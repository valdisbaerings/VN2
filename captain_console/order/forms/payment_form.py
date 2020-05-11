from django import forms


class PaymentForm(forms.Form):
    cardholdername = forms.CharField(label='Name of cardholder', max_length=100)
    cardno = forms.CharField(label='Card number', max_length=16)
    expdate = forms.CharField(label='Expiration date', max_length=5)
    cvc = forms.CharField(label='CVC', max_length=4)
