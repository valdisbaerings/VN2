from django import forms
from django.contrib.auth.forms import AuthenticationForm

class AdminAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_superuser:
            raise forms.ValidationError('User is not authorized')



