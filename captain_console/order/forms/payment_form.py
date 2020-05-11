from django import forms

class PaymentForm(forms.Form):
    cardholdername = forms.CharField(label='name of Cardholder', max_length=100)
    cardno = forms.IntegerField(label= 'cardno', min_value=0, min_digits=5, max_digits=5)
    expdate = forms.CharField(label='expdate', min_value = 0, min_digits=5, max_length=5)
    cvc = forms.IntegerField(label= 'cvc', min_value=0, min_digits=3, max_digits=3)