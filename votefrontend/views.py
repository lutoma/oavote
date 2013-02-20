# coding: utf-8

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.core.urlresolvers import reverse
from django.core.exceptions import PermissionDenied
from vote.models import User

def check_ident(function):
	"""
	A decorator function that checks the supplied token and adds a user object
	if the token was found
	"""

	def wrapper(*args):
		try:
			token = args[0].COOKIES['oa_token']
			function.__globals__['user'] = User.objects.get(token = token)

		except (KeyError, User.DoesNotExist):
			raise PermissionDenied

		if not user.token == token:
			raise PermissionDenied

		return function(*args)

	wrapper.__doc__= function.__doc__
	return wrapper

def ident(request, token):
	"""
	Stores the supplied token in a cookie so it doesn't have to be passed on in
	the url every time we reload a page
	"""

	response = HttpResponseRedirect(reverse('votefrontend.views.welcome'))
	response.set_cookie('oa_token', token)
	return response

@check_ident
def welcome(request):
	"""
	The welcome page displayed to users as soon as they have authenticated using
	their token
	"""

	response = render_to_response('votefrontend/welcome.html',
		context_instance = RequestContext(request, {'user': user}))

	return response
