from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime

from players.models import Player
from seasons.models import Season
from teams.models import Team
from leagues.models import LeagueMember
from .models import Match


class MatchForm(forms.ModelForm):
    player_1 = forms.ModelChoiceField(queryset=Player.objects.all())
    player_2 = forms.ModelChoiceField(queryset=Player.objects.all())
    player_3 = forms.ModelChoiceField(queryset=Player.objects.all())
    player_4 = forms.ModelChoiceField(queryset=Player.objects.all())

    class Meta:
        model = Match
        fields = ('player_1', 'player_2', 'player_3', 'player_4',
                  'team_1_score', 'team_2_score', 'completed',)

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        super(MatchForm, self).__init__(*args, **kwargs)
        league_players = LeagueMember.objects.filter(league=request.league).values_list('id', flat=True)
        self.fields['player_1'].queryset = Player.objects.filter(id__in=league_players)
        self.fields['player_2'].queryset = Player.objects.filter(id__in=league_players)
        self.fields['player_3'].queryset = Player.objects.filter(id__in=league_players)
        self.fields['player_4'].queryset = Player.objects.filter(id__in=league_players)

    # def clean(self):
    # data = super(MatchForm, self).clean()
    # players = set([data['player_1'].id, data['player_2'].id, data['player_3'].id, data['player_4'].id])
    # if len(players) != 4:
    # raise ValidationError('You must select 4 different players')
    #     return True
