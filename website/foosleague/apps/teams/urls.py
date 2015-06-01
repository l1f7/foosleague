from django.conf.urls import patterns, url
from .views import TeamListView, TeamDetailView, TeamUpdateView


urlpatterns = patterns('',
                       url(r'^$', TeamListView.as_view(), name='teams'),
                       url(r'^(?P<pk>[0-9]+)/$', TeamDetailView.as_view(), name='team-detail'),
                       url(r'^(?P<pk>[0-9]+)/edit/$', TeamUpdateView.as_view(), name='team-update'),
                       )
