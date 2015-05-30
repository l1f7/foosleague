from django.shortcuts import get_object_or_404
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.messages import success

from mixins.views import LoginRequiredMixin
from players.models import Player

from .forms import BetForm
from .models import Bet


class BetListView(LoginRequiredMixin, ListView):
    model = Bet
    template_name = "bookie/list.html"


class BetDetailView(LoginRequiredMixin, DetailView):
    model = Bet
    template_name = "bookie/detail.html"


class BetCreateView(LoginRequiredMixin, CreateView):
    model = Bet
    template_name = "bookie/create.html"
    form_class = BetForm

    def get_form(self, *args, **kwargs):
        form = self.form_class(self.request.POST or None)
        return form

    def form_valid(self, form, *args, **kwargs):
        bet = form.save(commit=False)
        player = get_object_or_404(Player, user=self.request.user)
        bet.player = player
        bet.save()
        success(self.request, "Bet has been placed! Good luck!")

        return HttpResponseRedirect(reverse_lazy('match-detail', kwargs={'pk': bet.match.id}))
