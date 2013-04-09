from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.core.urlresolvers import reverse
from django.core.exceptions import PermissionDenied
from vote.models import Poll, PollQuestion, Vote, User
from django.views.decorators.http import require_POST, require_safe

def poll_result(request, poll_id):
	"""
	Displays the results of a poll
	"""

	poll = get_object_or_404(Poll, id = poll_id)

	if poll.active and not request.user.is_superuser:
		raise PermissionDenied

	questions = PollQuestion.objects.filter(poll = poll)
	questions = questions.order_by('id')
	votes = Vote.objects.filter(poll_question__poll = poll)
	users = User.objects.filter(poll = poll)

	context = {'questions': questions, 'poll': poll, 'votes': votes, 'users': users}

	return render_to_response('voteresults/poll_result.html',
		context_instance = RequestContext(request, context))
