from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'fertilizer.views.home', name='home'),
    url(r'^thankyou/', 'fertilizer.views.thankyou', name='thankyou'),
    url(r'^states/', 'fertilizer.views.states', name='states'),
    url(r'^register/', 'fertilizer.views.register', name='register'),
    
    
    #url(r'^flot/', 'stats.views.statitics', name='stats'),
    #url(r'^indexa/', 'fertilizer.views.zeroa', name='indexa'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
