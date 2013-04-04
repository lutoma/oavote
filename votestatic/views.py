# coding: utf-8

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.core.urlresolvers import reverse
from django.core.exceptions import PermissionDenied
from vote.models import User, PollQuestion, Vote
from django.views.decorators.http import require_POST, require_safe

@require_safe
def index(request):
	"""
	The index page that displays some information
	"""

	response = render_to_response('votestatic/index.html',
		context_instance = RequestContext(request, {}))

	return response

@require_safe
def info(request):
	"""
	Info page
	"""

	response = render_to_response('votestatic/info.html',
		context_instance = RequestContext(request, {}))

	return response
