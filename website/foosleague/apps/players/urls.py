from django.conf.urls import patterns, url
from .views import PlayerListView, PlayerUpdateView, PlayerDetailView


urlpatterns = patterns('',
                       url(r'^$', PlayerListView.as_view(), name='players'),
                       url(r'^settings/$', PlayerUpdateView.as_view(), name='players-update'),
                       url(r'^(?P<pk>[0-9])/$', PlayerDetailView.as_view(), name='player-detail')
                       )
