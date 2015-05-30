from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from mixins.views import LoginRequiredMixin
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
    template_name= 'matches/create.html'

    def get_form(self, *args, **kwargs):
        form = self.form_class(self.request.POST or None)
        return form
