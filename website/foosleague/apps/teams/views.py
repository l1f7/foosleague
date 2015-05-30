from django.views.generic.list import ListView
from .models import Team


class TeamListView(ListView):
    model = Team
    template_name = "teams/list.html"
