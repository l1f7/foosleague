from django.conf.urls import patterns, url
from .views import SeasonListView, SeasonDetailView

urlpatterns = patterns('',
                       url(r'^$', SeasonListView.as_view(), name='seasons'),
                       url(r'^(?P<pk>[0-9]+)/$', SeasonDetailView.as_view(), name='seasons-detail')
                       )
