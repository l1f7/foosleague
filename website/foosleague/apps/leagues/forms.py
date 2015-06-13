from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime

from .models import League


class LeagueForm(forms.ModelForm):

    class Meta:
        model = League

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        super(LeagueForm, self).__init__(*args, **kwargs)
