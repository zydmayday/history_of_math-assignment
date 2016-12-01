from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'my_blog.views.home', name='home'),
    url(r'^about$', 'my_blog.views.about', name='about'),
    url(r'^', include('article.urls')),
    url(r'^', include('history.urls')),
    url(r'^fantesysix', include('fantesysix.urls')),
    url(r'^runfast', include('runfast.urls')),
    url(r'^spider', include('spider.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
