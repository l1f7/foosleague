import urllib2
import re
import requests

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
                match.winner = match.team_1
            else:
                match.team_2.streak += 1
                match.team_2.save()
                match.winer = match.team_2

            match.save()

            success(self.request, "Match has ended! Congrats team %s" % (match.winner,))
            return HttpResponseRedirect(reverse_lazy('match-detail', kwargs={'pk': match.id}))

        else:
            error(self.request, "You must be apart of this match to close the game.")
            return HttpResponseRedirect(reverse_lazy('match-detail', kwargs={'pk': match.id}))


def generate_name():
    response = urllib2.urlopen("http://www.teamnames.net/fantasy/random-team-name-generator", timeout=5)
    html = response.read()
    result = re.search('(?<=_track\[\'generator\'\] =).*', html)
    name = result.group(0)

    return name.split("'")[1]


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
        # team_1, _ = Team.objects.get_or_create(players__in=[form.cleaned_data['player_1'], form.cleaned_data['player_2']])
        # team_2, _ = Team.objects.get_or_create(players__in=[form.cleaned_data['player_3'], form.cleaned_data['player_4']])

        p1 = form.cleaned_data['player_1']
        p2 = form.cleaned_data['player_2']
        p3 = form.cleaned_data['player_3']
        p4 = form.cleaned_data['player_4']

        p1_teams = Team.objects.filter(players=p1,)
        p2_teams = Team.objects.filter(players=p2,)

        team_1 = None
        for p in p1_teams:
            if p in p2_teams:
                team_1 = p

        if not team_1:

            team_1 = Team.objects.create(name='%s' % (generate_name(),))
            team_1.players.add(p1)
            team_1.players.add(p2)
            team_1.save()

        p3_teams = Team.objects.filter(players=p3)
        p4_teams = Team.objects.filter(players=p4)

        team_2 = None
        for p in p3_teams:
            if p in p4_teams:
                team_2 = p

        if not team_2:
            # generate_name

            team_2 = Team.objects.create(name='%s' % (generate_name(),))
            team_2.players.add(p3)
            team_2.players.add(p4)
            team_2.save()

        seasons = Season.objects.filter(start__gte=date, end__lte=date)
        season = None
        if seasons.count():
            season = seasons[0]

        match = Match(team_1=team_1, team_2=team_2,
                      team_1_score=form.cleaned_data[
                          'team_1_score'], team_2_score=form.cleaned_data['team_2_score'],
                      completed=form.cleaned_data['completed'], season=season)

        if form.cleaned_data['completed']:
            if form.cleaned_data['team_1_score'] > form.cleaned_data['team_2_score']:
                match.winner = team_1
                loser = team_2
                winning_score = match.team_1_score
                losing_score = match.team_2_score
            elif form.cleaned_data['team_2_score'] > form.cleaned_data['team_1_score']:
                match.winner = team_2
                loser = team_1
                winning_score = match.team_2_score
                losing_score = match.team_1_score
            requests.post('https://liftinteractive.slack.com/services/hooks/slackbot?token=cPqfDDQsk7QJ71ofvpy4aqF4&channel=%23test',

                          data="Game Over! *%s* defeats _%s_ ( *%s* - _%s_ )" % (match.winner, loser, winning_score, losing_score))

            match.save()
            match.complete()
        else:
            #post to slack!

            requests.post('https://liftinteractive.slack.com/services/hooks/slackbot?token=cPqfDDQsk7QJ71ofvpy4aqF4&channel=%23test',
                          data="Game on! *%s* _(%s)_ vs *%s* _(%s)_" % (match.team_1, match.team_1.streak, match.team_2, match.team_2.streak))

        match.save()

        success(self.request, "Match has been created!")
        return HttpResponseRedirect(reverse_lazy('match-detail', kwargs={'pk': match.id}))
