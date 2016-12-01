from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

	url(r'^history$', 'history.views.history', name='history.views.history'),
)