from django.conf.urls import patterns, url
from .views import LeagueCreateView, LeagueUpdateView, LeagueListView

urlpatterns = patterns('',
                       url(r'^leagues/$', LeagueListView.as_view(), name='leagues'),
                       url(r'^leagues/create/$', LeagueCreateView.as_view(), name='league-create'),
                       url(r'^update/$', LeagueUpdateView.as_view(), name='league-create'),


)
