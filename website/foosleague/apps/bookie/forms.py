from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime
from datetime import timedelta
from .models import Bet

from matches.models import Match


class BetForm(forms.ModelForm):

    class Meta:
        model = Bet
        fields = ('amount', 'match',)

    def __init__(self, *args, **kwargs):
        super(BetForm, self).__init__(*args, **kwargs)
        # you can only bet on a match until when... 2 minutes? first goal?
        # todo: Filter matches that you are not apart of

        self.fields['match'].queryset = Match.objects.filter(
            created__gte=datetime.now() - timedelta(minutes=2), completed=False)

    def clean_match(self):
        # make sure user is betting on their own match :o
        #.... although, if you are betting for yourself to win...... at least it aligns with your motivations
        if self.request.user.id in self.cleaned_data['match'].players.values_list('user__id', flat=True):
            raise ValidationError("You can't bet on your own match.")

        return True

    def clean_amount(self):
        if self.cleaned_data['amount'] <= 0:
            raise ValidationError("You can't bet negative amounts. Nice try though.")

        return True
