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
    
    url(r'^$', 'keyval.core.views.index', name='index'),
    url(r'^api/$', direct_to_template, {'template': 'core/api.html'}, name='api'),
    url(r'^account/$', 'keyval.core.views.account', name='account'),
    
    url(r'^login/$', 'django.contrib.auth.views.login', { 
        'template_name': 'core/login.html' 
    }, name='login'),
    
    url(r'^logout/$', 'django.contrib.auth.views.logout', {
        'template_name': 'core/logout.html', 
        'next_page': '/' 
    }, name='logout'),
)

from django.conf import settings

if settings.SERVE_STATIC:
    urlpatterns += patterns('',
        # Serve media through Django (not to be used in production, controlled via settings.SERVE_STATIC)
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT }),
    )

# The username matching must be performed last as the expressions are very general.
urlpatterns += patterns('',
    url(r'^(?P<username>[^/]+)/(?P<key>[^/]+)/edit/$', 'keyval.core.views.keyval_edit', name='keyval_edit'),
    url(r'^(?P<username>[^/]+)/(?P<key>[^/]+)/$', 'keyval.core.views.keyval_profile', name='keyval_profile'),
    url(r'^(?P<username>[^/]+)/$', 'keyval.core.views.user_profile', name='user_profile'),
)