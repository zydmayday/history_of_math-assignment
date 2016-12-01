from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

	url(r'^$', 'runfast.views.home', name='runfast.views.home'),
	url(r'^join$', 'runfast.views.join', name='runfast.views.join'),
	url(r'^game$', 'runfast.views.game', name='runfast.views.game'),
	url(r'^play$', 'runfast.views.play', name='runfast.views.play'),
	url(r'^passTurn$', 'runfast.views.passTurn', name='runfast.views.passTurn'),
	url(r'^reset$', 'runfast.views.reset', name='runfast.views.reset'),
)