from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime

from .models import Bet


class BetForm(forms.ModelForm):

    class Meta:
        model = Bet
        fields = ('amount', 'match',)

    def clean_match(self):
        # make sure user is betting on their own match :o
        if self.request.user in self.match.player__set.values_list('user', flat=True):
            raise ValidationError("You can't bet on your own match.")

        return True

    def clean_amount(self):

        return True