from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

	url(r'^douban/callback/$', 'spider.views.callback', name='spider.views.callback'),
	
)