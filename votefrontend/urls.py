from django.conf.urls import patterns, include, url

"""
The URL parts after /vote/. For the rest, see aovote/urls.py
"""

urlpatterns = patterns('',
	url(r'^ident/(?P<token>[^\/]+)/$', 'votefrontend.views.ident', name='ident'),
	url(r'^welcome/$', 'votefrontend.views.welcome', name='welcome'),
)
