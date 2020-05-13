from django import forms


class PaymentForm(forms.Form):
    cardholdername = forms.CharField(label='Name of cardholder', max_length=100)
    cardno = forms.CharField(label='Card number', max_length=16, min_length=15,
                             widget=forms.TextInput(attrs={'pattern': '[0-9]+', 'title': 'Enter numbers only'}))
    expdate = forms.CharField(label='Expiration date', help_text='[MM/YY]', widget=forms.TextInput(
        attrs={'pattern': "(?:0[1-9]|1[0-2])/[0-9]{2}", 'title': 'Please use the format: [MM/YY]'}))
    cvc = forms.CharField(label='CVC', max_length=4, min_length=3)
