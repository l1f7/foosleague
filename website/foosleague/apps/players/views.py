from django.db.models import Q
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from .models import Player
from teams.models import Team
from matches.models import Match


class PlayerListView(ListView):
    model = Player
    template_name = "players/list.html"


class PlayerUpdateView(UpdateView):
    model = Player
    template_name = "players/update.html"


class PlayerDetailView(DetailView):
    model = Player
    template_name = "players/detail.html"

    def get_context_data(self, *args, **kwargs):
        c = super(PlayerDetailView, self).get_context_data(*args, **kwargs)
        player = self.get_object()
        teams = Team.objects.filter(players=player)
        c['teams'] = teams
        c['matches'] = Match.objects.filter(Q(team_1__in=teams) | Q(team_2__in=teams))
        c['wins'] = c['matches'].filter(winner__in=c['teams'])
        c['loses'] = c['matches'].count() - c['wins']

        return c
