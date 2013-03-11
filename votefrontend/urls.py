from django.conf.urls import patterns, include, url

"""
The URL parts after /vote/. For the rest, see oavote/urls.py
"""

urlpatterns = patterns('',
	url(r'^ident/(?P<token>[^\/]+)/$', 'votefrontend.views.ident', name='ident'),
	url(r'^welcome/$', 'votefrontend.views.welcome', name='welcome'),
	url(r'^question/(?P<question_id>[0-9]+)/$', 'votefrontend.views.show_question', name='show_question'),
	url(r'^question/(?P<question_id>[0-9]+)/vote/$', 'votefrontend.views.submit_vote', name='submit_vote'),
	url(r'^thanks/$', 'votefrontend.views.thanks', name='thanks'),
)
