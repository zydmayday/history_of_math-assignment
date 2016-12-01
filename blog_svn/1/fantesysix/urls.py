from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

	url(r'^$', 'fantesysix.views.home', name='fantesysix.views.home'),
	url(r'^judge$', 'fantesysix.views.judge', name='fantesysix.views.judge'),
	
)