from .models import Player
from django import forms
from django.core.exceptions import ValidationError


class PlayerForm(forms.ModelForm):
    current_password = forms.CharField(widget=forms.PasswordInput, label='Current Password', required=False)
    password1= forms.CharField(widget=forms.PasswordInput, label="New Password", required=False)
    password2 = forms.CharField(widget=forms.PasswordInput, label="Repeat New Password", required=False)


    class Meta:
        model = Player
        fields = ['nickname', 'photo', 'slack_username', 'current_password', 'password1', 'password2']
    def clean_password1(self):
            data = self.cleaned_data['password1']
            self.pass1 = data
            if self.cleaned_data['current_password']:
                if not self.instance.user.check_password(self.cleaned_data['current_password']):
                    raise ValidationError('Current pasword incorrect')
            return data


    def clean_password2(self):
        data = self.cleaned_data['password2']

        if data != self.pass1:
            raise ValidationError('New passwords do not match.')

        return data


    def save(self, commit=True):
        """
        Saves the new password.
        """
        super(PlayerForm, self).save(commit)

        if self.cleaned_data['current_password']:
            self.instance.user.set_password(self.cleaned_data["password1"])

        if commit:
            self.instance.user.save()
            self.instance.save()

        return self.instance