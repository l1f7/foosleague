from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Season


class SeasonListView(ListView):
    model = Season
    template_name = "seasons/list.html"


class SeasonDetailView(DetailView):
    model = Season
    template_name = "seasons/detail.html"

# todo
   # Create Seasons
   # Manage seasons
