from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label="Username", required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password", required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, label="Repeat Password", required=True)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name')

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise ValidationError('Passwords do not match')
        else:
            if len(self.cleaned_data['password2']) < 5:
                raise ValidationError('Passwords must be at least 5 characters long')

        return self.cleaned_data['password2']
