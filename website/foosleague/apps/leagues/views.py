from django.http.response import Http404, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.messages import success, error

from mixins.views import LoginRequiredMixin
from players.models import Player
from leagues.models import League, LeagueMember
from leagues.forms import LeagueForm

# todo
# league update
# league invite
# league member management
#   - remove, promote/demote to admin


class LeagueCreateView(LoginRequiredMixin, CreateView):
    model = League
    template_name = "leagues/create.html"
    form_class = LeagueForm

    def form_valid(self, form):
        league = form.save()
        lm = LeagueMember.objects.create(league=league, player=self.request.player, admin=True)

        success(self.request, "League has been created")

        return HttpResponseRedirect('http://%s.foosleague.com/' % (league.subdomain,))


class LeagueUpdateView(LoginRequiredMixin, UpdateView):
    model = League
    template_name = "leagues/update.html"
    form_class = LeagueForm

    def get_object(self, *args, **kwargs):
        obj = self.request.league
        player = self.request.player
        member = LeagueMember.objects.filter(league=obj, player=player, admin=True)
        if not member.count():
            raise Http404

        return obj

    def get_form(self, *args, **kwargs):
        return self.form_class(self.request.POST or None, self.request.FILES or None, instance=self.get_object(), request=self.request)


class LeagueListView(LoginRequiredMixin, ListView):
    model = League
    template_name = "leagues/list.html"

    def get_queryset(self, *args, **kwargs):
        qs = super(LeagueListView, self).get_queryset(*args, **kwargs)
        player = Player.objects.filter(user=self.request.user)
        qs = qs.filter(id__in=LeagueMember.objects.filter(player=player).values_list('league__id', flat=True))
