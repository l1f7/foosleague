from django.conf.urls import patterns, url
from .views import BetListView, BetDetailView, BetCreateView


urlpatterns = patterns('',
                       url(r'^$', BetListView.as_view(), name='bets'),
                       url(r'^create/$', BetCreateView.as_view(), name='bet-create'),
                       url(r'^(?P<pk>[0-9])/$', BetDetailView.as_view(), name='bet-detail'),
                       )
