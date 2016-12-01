from django.conf.urls import patterns, include, url
from hitcount.views import update_hit_count_ajax

urlpatterns = patterns('',

	url(r'^articles$', 'article.views.articles', name='article.views.articles'),
	url(r'^article/(?P<article_id>\d+)$', 'article.views.article', name='article.views.article'),
	url(r'^article/add$', 'article.views.add_article', name='article.views.add_article'),
	url(r'^article/edit/list$', 'article.views.edit_article_list', name='article.views.edit_article_list'),
	url(r'^article/edit/(?P<article_id>\d+)$', 'article.views.edit_article', name='article.views.edit_article'),

	url(r'^label/add$', 'article.views.add_label', name='article.views.add_label'),

	url(r'^label/(?P<label_id>\d+)$', 'article.views.label', name='article.views.label'),

	url(r'^timeline/add$', 'article.views.add_timeline', name='article.views.add_timeline'),
	url(r'^timeline$', 'article.views.get_timelines', name='article.views.get_timelines'),

	url(r'^quicknote$', 'article.views.get_quicknotes', name='article.views.get_quicknotes'),
	url(r'^quicknote/(?P<quicknote_id>\d+)$', 'article.views.get_quicknotes_by_ajax', name='article.views.get_quicknotes_by_ajax'),
	
	# hitcount configuration
	url(r'^ajax/hit/$', update_hit_count_ajax, name='hitcount_update_ajax'), # keep this name the same
)