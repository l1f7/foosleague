from django.conf.urls import patterns, url
from .views import MatchListView, MatchDetailView, MatchCreateView, MatchUpdateView

urlpatterns = patterns('',
                       url(r'^$', MatchListView.as_view(), name='matches'),
                       url(r'^create/$', MatchCreateView.as_view(), name='match-create'),
                       url(r'^(?P<pk>[0-9]+)/$', MatchDetailView.as_view(), name='match-detail'),
                       url(r'^(?P<pk>[0-9]+)/update/$', MatchUpdateView.as_view(), name='match-update'),

                       # url(r'^(?P<pk>[0-9])/complete/$', MatchCompleteView.as_view(), name='match-complete')
                       )
