from django.conf import settings
from django.conf.urls import patterns, include, url, static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

import adminactions.actions as actions


actions.add_to_site(admin.site)

urlpatterns = patterns('',
    url(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    url(r'^foosadmin/', include(admin.site.urls)),

    url(r'^teams/', include('teams.urls')),
    url(r'^players/', include('players.urls')),
    url(r'^matches/', include('matches.urls')),
    url(r'^seasons/', include('seasons.urls')),
    url(r'^robots\.txt/$', TemplateView.as_view(template_name='robots.txt',
        content_type='text/plain')),

    (r'^adminactions/', include('adminactions.urls')),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static.static(
      settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += (
      url(r'^404/$', 'django.views.defaults.page_not_found'),
      url(r'^500/$', 'django.views.defaults.server_error')
    )
