from django.conf.urls import patterns, url
from .views import TeamListView


urlpatterns = patterns('',
                       url(r'^$', TeamListView.as_view(), name='teams'),
                       )
