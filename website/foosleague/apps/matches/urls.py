from django.conf.urls import patterns, url
from .views import MatchListView, MatchDetailView, MatchCreateView, MatchUpdateView, MatchScoreUpdateView, MatchCompleteView

urlpatterns = patterns('',
                       url(r'^$', MatchListView.as_view(), name='matches'),
                       url(r'^create/$', MatchCreateView.as_view(), name='match-create'),
                       url(r'^(?P<pk>[0-9]+)/$', MatchDetailView.as_view(), name='match-detail'),
                       url(r'^(?P<pk>[0-9]+)/update/$', MatchUpdateView.as_view(), name='match-update'),
                       url(r'^(?P<pk>[0-9]+)/complete/$', MatchCompleteView.as_view(), name='match-complete'),

                       url(r'^goal/(?P<team>[a-zA-Z]+)/(?P<score>[1\-]+)/$', MatchScoreUpdateView.as_view(), name='score-update'),
                       url(r'^scoreupdate/(?P<team>[a-zA-Z]+)/$', MatchScoreUpdateView.as_view(), name='score-update'),
                       # url(r'^(?P<pk>[0-9])/complete/$', MatchCompleteView.as_view(), name='match-complete')
                       )
