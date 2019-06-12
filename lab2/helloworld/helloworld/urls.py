from django.conf.urls import patterns, include, url
#from django.http import HttpResponse
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'flatpages.views.home', name='home'),
    url(r'^hello/$','flatpages.views.home', name='home'),                   
    url(r'^admin/', include(admin.site.urls)),
)
