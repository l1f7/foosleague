from django import forms
from django.core.exceptions import ValidationError

from .models import Team


class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = ('name', 'logo')

