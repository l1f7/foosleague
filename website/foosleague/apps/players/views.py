from django.db.models import Q
from django.http.response import Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from mixins.views import LoginRequiredMixin
from .models import Player
from teams.models import Team
from matches.models import Match
from leagues.models import LeagueMember
from django.shortcuts import get_object_or_404
from datetime import datetime
from seasons.models import Season

from .forms import PlayerForm


class PlayerListView(ListView):
    model = Player
    template_name = "players/list.html"

    def get_queryset(self, *args, **kwargs):
        qs = super(PlayerListView, self).get_queryset(*args, **kwargs)
        date = datetime.today()

        seasons = Season.objects.filter(start__lte=date, end__gte=date)


        return qs.filter(id__in=LeagueMember.objects.filter(league=self.request.league).values_list('player__id', flat=True)).filter(id__in=Match.objects.filter(season=seasons[0]).values_list('team_1__players__id', flat=True)).filter(id__in=Match.objects.filter(season=seasons[0]).values_list('team_2__players__id', flat=True))



class PlayerUpdateView(LoginRequiredMixin, UpdateView):
    model = Player
    template_name = "players/update.html"
    form_class = PlayerForm
    def get_object(self, *args, **kwargs):
        obj = super(PlayerUpdateView, self).get_object(*args, **kwargs)
        if obj.user != self.request.user:
            raise Http404
        return obj

class PlayerDetailView(DetailView):
    model = Player
    template_name = "players/detail.html"

    def get_object(self, *args, **kwargs):
        obj = get_object_or_404(Player.objects.select_related(), pk=self.kwargs['pk'])

        if obj.id not in LeagueMember.objects.filter(league=self.request.league).values_list('player__id', flat=True):
            raise Http404
        return obj


    def get_context_data(self, *args, **kwargs):
        c = super(PlayerDetailView, self).get_context_data(*args, **kwargs)
        player = self.get_object()
        teams = Team.objects.filter(players=player)
        c['teams'] = teams
        c['matches'] = Match.objects.filter(Q(team_1__in=teams) | Q(team_2__in=teams), league=self.request.league)
        c['wins'] = c['matches'].filter(winner__in=c['teams']).count()
        c['loses'] = c['matches'].count() - c['wins']

        return c

