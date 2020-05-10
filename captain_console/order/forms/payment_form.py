from django import forms

class PaymentForm(forms.Form):
    cardholdername = forms.CharField(label='name of Cardholder', max_length=100)
    cardno = forms.IntegerField(label= 'cardno', min_value=16, max_value=16)
    expdate = forms.CharField(label='expdate', min_value=5, max_length=5)
    cvc = forms.IntegerField(label= 'cvc', min_value=3, max_value=3)