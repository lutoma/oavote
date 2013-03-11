from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'votestatic.views.index', name='index'),
)
