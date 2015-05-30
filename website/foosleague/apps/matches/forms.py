from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime

from players.models import Player
from seasons.models import Season
from teams.models import Team
from .models import Match


class MatchForm(forms.ModelForm):
    player_1 = forms.ModelChoiceField(queryset=Player.objects.all())
    player_2 = forms.ModelChoiceField(queryset=Player.objects.all())
    player_3 = forms.ModelChoiceField(queryset=Player.objects.all())
    player_4 = forms.ModelChoiceField(queryset=Player.objects.all())

    class Meta:
        model = Match
        fields = ('player_1', 'player_2', 'player_3', 'player_4', 'team_1_score', 'team_2_score')

    def clean(self):
        data = super(MatchForm, self).clean()
        players = set([data['player_1'].id, data['player_2'].id, data['player_3'].id, data['player_4'].id])
        if players.count() != 4:
            raise ValidationError('You must select 4 different players')
        return True

    def is_valid(self):
        match = self.save(commit=False)
        date = datetime.today()

        seasons = Season.objects.filter(start__gte=date, end__lte=date)
        if seasons.count():
            match.seasons = seasons[0]



        match.save()
