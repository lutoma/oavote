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
	votes = Vote.objects.filter(poll_question__poll = poll)
	users = User.objects.filter(poll = poll)


	# Distinct with field names is only supported by Postgres
	try:
		votingusers = votes.distinct('voting_user').count()
	except NotImplementedError:
		# Emulate DISCTINCT ON function of Postgres by writing in a dictionary
		# with the user as the key, thus only overwriting if a user voted
		# multiple times instead of getting duplicates
		temp_users = {}

		for vote in votes:
			temp_users[vote.voting_user] = True

		votingusers = len(temp_users)
		del temp_users

	context = {
		'questions': questions.order_by('id'),
		'poll': poll,
		'votes': votes,
		'users': users,
		'maxvotes': users.count() * questions.count(),
		'votingusers': votingusers,
		'votingpercentage': round(float(votingusers) / float(users.count()) * 100, 2),
	}

	return render_to_response('voteresults/poll_result.html',
		context_instance = RequestContext(request, context))
