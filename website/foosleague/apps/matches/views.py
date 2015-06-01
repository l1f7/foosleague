from datetime import datetime
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.messages import success, error

from mixins.views import LoginRequiredMixin

from teams.models import Team
from seasons.models import Season
from players.models import Player
from .models import Match
from .forms import MatchForm


class MatchListView(LoginRequiredMixin, ListView):
    model = Match
    template_name = "matches/list.html"


class MatchDetailView(LoginRequiredMixin, DetailView):
    model = Match
    template_name = "matches/detail.html"


class MatchCompleteView(LoginRequiredMixin, DetailView):
    model = Match

    def get(self, *args, **kwargs):
        if self.request.user == self.player_1.user or self.request.user == self.player_2.user:
            match = self.get_object()
            match.complete = True
            match.save()
            if match.team_1_score > match.team_2_score:
                match.team_1.streak += 1
                match.team_1.save()
                winner = match.team_1
            else:
                match.team_2.streak += 1
                match.team_2.save()
                winner = match.team_2

            success(self.request, "Match has ended! Congrats team %s" % (winner,))
            return HttpResponseRedirect(reverse_lazy('match-detail', kwargs={'pk': match.id}))

        else:
            error(self.request, "You must be apart of this match to close the game.")
            return HttpResponseRedirect(reverse_lazy('match-detail', kwargs={'pk': match.id}))


class MatchCreateView(LoginRequiredMixin, CreateView):
    model = Match
    form_class = MatchForm
    template_name = 'matches/create.html'

    def get_form(self, *args, **kwargs):
        form = self.form_class(self.request.POST or None)
        return form

    def get_context_data(self, *args, **kwargs):
        c = super(MatchCreateView, self).get_context_data(*args, **kwargs)
        # will eventually be filtered by league..
        c['players'] = Player.objects.all()
        return c

    def form_valid(self, form, *args, **kwargs):

        date = datetime.today()
        # team_1, _ = Team.objects.get_or_create(players__in=[self.cleaned_data['player_1'], self.cleaned_data['player_2']], id=1)
        # team_2, _ = Team.objects.get_or_create(players__in=[self.cleaned_data['player_3'], self.cleaned_data['player_4']], id=2)
        team_1 = Team.objects.get(id=1)
        team_2 = Team.objects.get(id=1)
        seasons = Season.objects.filter(start__gte=date, end__lte=date)
        season = None
        if seasons.count():
            season = seasons[0]

        match = Match(team_1=team_1, team_2=team_2,
                      team_1_score=form.cleaned_data[
                          'team_1_score'], team_2_score=form.cleaned_data['team_2_score'],
                      completed=form.cleaned_data['completed'], season=season)
        match.save()
        success(self.request, "Match has been created!")
        return HttpResponseRedirect(reverse_lazy('match-detail', kwargs={'pk': match.id}))

