from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from .models import Player


class PlayerListView(ListView):
    model = Player
    template_name = "players/list.html"


class PlayerUpdateView(UpdateView):
    model = Player
    template_name = "players/update.html"


class PlayerDetailView(DetailView):
    model = Player
    template_name = "players/detail.html"
