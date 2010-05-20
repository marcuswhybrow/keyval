from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template

# Autodisover the administration urls
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    url(r'^$', direct_to_template, {'template': 'core/index.html'}, name='index'),
    url(r'^account/$', direct_to_template, {'template': 'core/account.html'}, name='account'),
    url(r'^api/$', direct_to_template, {'template': 'core/api.html'}, name='api'),
)

from django.conf import settings

if settings.SERVE_STATIC:
    urlpatterns += patterns('',
        # Serve media through Django (not to be used in production, controlled via settings.SERVE_STATIC)
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT }),
    )

# The username matching must be performed last as the expressions are very general.
urlpatterns += patterns('',
    url(r'^(?P<username>[^/]+)/(?P<key>[^/]+)/$', 'keyval.core.views.keyval_profile', name='keyval_profile'),
    url(r'^(?P<username>[^/]+)/$', 'keyval.core.views.user_profile', name='user_profile'),
)