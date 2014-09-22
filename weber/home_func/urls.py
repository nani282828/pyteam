from django.conf.urls import patterns, include, url

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'weber.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^post_status$','home_func.views.post_status'),
    url(r'^load_more_posts','home_func.views.load_scroll_posts'),
    url(r'^search','home_func.views.search_titles'),
    url(r'^profile/(?P<username>[-\w]+)/$','home_func.views.profile_info'),
    #url(r'^profile/','home_func.views.profile_info'),
)
