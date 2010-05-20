from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
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

    url(r'^(?P<username>[^/]+)/(?P<key>[^/]+)/$', 'keyval.core.views.keyval_profile', name='keyval_profile'),
    url(r'^(?P<username>[^/]+)/$', 'keyval.core.views.user_profile', name='user_profile'),
)