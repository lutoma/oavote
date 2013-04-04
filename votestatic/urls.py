from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'votestatic.views.index', name='index'),
	url(r'^info/$', 'votestatic.views.info', name='info'),
)
