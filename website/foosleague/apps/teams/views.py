from django.shortcuts import get_object_or_404

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages import error, success
from django.http.response import HttpResponseRedirect
from django.db.models import Q

from mixins.views import LoginRequiredMixin
from matches.models import Match

from players.models import Player

from .models import Team
from .forms import TeamForm


class TeamListView(ListView):
    model = Team
    template_name = "teams/list.html"

    def get_queryset(self, *args, **kwargs):
        # teams_that_played
        return super(TeamListView, self).get_queryset(*args, **kwargs).filter(league=self.request.league,)


class TeamDetailView(DetailView):
    model = Team
    template_name = "teams/detail.html"

    def get_object(self, *args, **kwargs):
        return get_object_or_404(Team, pk=self.kwargs['pk'], league=self.request.league)

    def get_context_data(self, *args, **kwargs):
        c = super(TeamDetailView, self).get_context_data(*args, **kwargs)
        team = self.get_object()
        c['matches'] = Match.objects.filter(
            Q(team_1=team) | Q(team_2=team), league=self.request.league, season=self.request.season)
        c['wins'] = c['matches'].filter(winner=self.get_object()).count()
        c['losses'] = c['matches'].count() - c['wins']

        return c


class TeamUpdateView(LoginRequiredMixin, UpdateView):
    model = Team
    template_name = "teams/update.html"
    form_class = TeamForm

    def dispatch(self, *args, **kwargs):
        team = self.get_object()
        player = Player.objects.get(user=self.request.user)

        if player not in team.players.all():
            error(self.request, "You must be apart of this team to edit")
            return HttpResponseRedirect(reverse_lazy("team-detail", kwargs={'pk': team.id}))

        return super(TeamUpdateView, self).dispatch(*args, **kwargs)

    def get_form(self, *args, **kwargs):
        form = self.form_class(
            self.request.POST or None, self.request.FILES or None, instance=self.get_object())
        return form

    def form_valid(self, form):
        c = form.save()
        success(self.request, "%s successfully updated" % (c.name,))
        return HttpResponseRedirect(reverse_lazy('team-detail', kwargs={'pk': c.id}))
