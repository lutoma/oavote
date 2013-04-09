from django.conf.urls import patterns, include, url

"""
The URL parts after /vote/. For the rest, see oavote/urls.py
"""

urlpatterns = patterns('',
	url(r'^(?P<poll_id>[0-9]+)/$', 'voteresults.views.poll_result', name='poll_result'),
)
