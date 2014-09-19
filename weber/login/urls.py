from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'weber.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$','login.views.index'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': '/theweber.in/'}),
    url(r'^index$','login.views.index'),
    url(r'^register$','login.views.register'),
    url(r'^login$','login.views.login'),
    url(r'^home$','login.views.home'),
    #url(r'^logout$','login.views.logout_view'),

)
