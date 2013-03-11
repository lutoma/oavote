# coding: utf-8

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.core.urlresolvers import reverse
from django.core.exceptions import PermissionDenied
from vote.models import User, PollQuestion, Vote
from django.views.decorators.http import require_POST, require_safe

def check_ident(function):
	"""
	A decorator function that checks the supplied token and adds a user object
	if the token was found
	"""

	def wrapper(*args, **keyword_args):
		try:
			token = args[0].COOKIES['oa_token']
			function.__globals__['user'] = User.objects.get(token = token)
		except (KeyError, User.DoesNotExist):
			raise PermissionDenied

		# Double check just for the sake of it
		if not function.__globals__['user'].token == token:
			raise PermissionDenied

		return function(*args, **keyword_args)

	wrapper.__doc__= function.__doc__
	return wrapper

@require_safe
def ident(request, token):
	"""
	Stores the supplied token in a cookie so it doesn't have to be passed on in
	the url every time we reload a page
	"""

	response = HttpResponseRedirect(reverse('votefrontend.views.welcome'))
	response.set_cookie('oa_token', token)
	return response

@require_safe
@check_ident
def welcome(request):
	"""
	The welcome page displayed to users as soon as they have authenticated using
	their token
	"""

	first_question = PollQuestion.objects.filter(poll = user.poll).order_by('id')[0]
	context = {'token_user': user, 'question': first_question}

	response = render_to_response('votefrontend/welcome.html',
		context_instance = RequestContext(request, context))

	return response

@require_safe
@check_ident
def show_question(request, question_id):
	"""
	Displays a single question to vote upon
	"""

	question = get_object_or_404(PollQuestion,
		poll = user.poll,
		id = question_id)

	# Check if the user already voted on this (To show info message in template)
	try:
		vote = Vote.objects.get(voting_user = user, poll_question = question)
	except Vote.DoesNotExist:
		vote = None

	context = {'user': user, 'question': question, 'vote': vote}
	response = render_to_response('votefrontend/question.html',
		context_instance = RequestContext(request, context))

	return response

@require_POST
@check_ident
def submit_vote(request, question_id):
	"""
	Submits a vote that has been made in the show_question view
	"""

	question = get_object_or_404(PollQuestion,
		poll = user.poll,
		id = question_id)

	valid_choices = {'yes': 0, 'no': 1, 'abstention': 2}

	# Check if the vote key exists and contains a valid value
	if not 'vote' in request.POST or not request.POST['vote'] in valid_choices:
		return HttpResponseRedirect(reverse('show_question', kwargs = {'question_id': question.id}))

	# Check if user already voted on this. If not, create new Vote object
	try:
		vote = Vote.objects.get(voting_user = user, poll_question = question)
	except Vote.DoesNotExist:
		vote = Vote(voting_user = user, poll_question = question)

	vote.choice = valid_choices[request.POST['vote']]
	vote.save()

	next_question = question.next()
	
	if next_question == None:
		return HttpResponseRedirect(reverse('thanks'))

	return HttpResponseRedirect(reverse('show_question', kwargs = {'question_id': next_question.id}))

@require_safe
@check_ident
def thanks(request):
	"""
	The page that's displayed after a user finished voting
	"""

	context = {'token_user': user}

	response = render_to_response('votefrontend/thanks.html',
		context_instance = RequestContext(request, context))

	# Delete authorization cookie
	response.delete_cookie('oa_token')
	return response
