# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid

class Poll(models.Model):
	"""
	A poll round which has several questions (PollQuestion) which will be voted
	on.
	"""

	created_at = models.DateTimeField(
		auto_now_add = True,
		verbose_name = _('Created at'))

	title = models.CharField(max_length = 400, verbose_name = ('Title'))
	active = models.BooleanField(verbose_name = _('Active'))

	def __unicode__(self):
		return self.title


class User(models.Model):
	"""
	A user which is allowed to vote. It is authenticated by a token which gets
	sent to it by email. The first name is stored for a personalised greeting in
	the email. The member ID is stored so the user may check if it's vote has
	been stored correctly later.

	Please note that users are specific to single polls and are only used once.
	"""

	poll = models.ForeignKey(Poll, verbose_name = _('Corresponding poll'))
	used = models.BooleanField(verbose_name = _('Token used?'))
	mail_sent = models.BooleanField(verbose_name = _('Mail sent?'))

	email_address = models.EmailField(
		max_length = 254,
		verbose_name = _('Email address'))

	first_name = models.CharField(
		max_length = 400,
		verbose_name = _('First name'))

	member_id = models.IntegerField(verbose_name = _('Member ID'))

	def get_token():
		"Generates a single token"
		return uuid.uuid4().__str__()

	token = models.CharField(
		max_length = 36,
		verbose_name = _('Auth token'),
		default = get_token)
	
	voting_ip = models.GenericIPAddressField(
		unpack_ipv4 = True,
		verbose_name = _('Login IP'),
		blank = True,
		null = True)

	def __unicode__(self):
		return '#{}'.format(self.member_id)

class PollQuestion(models.Model):
	"""
	A single question. These are shown to the users, which can answer it with
	yes/no/abstention.
	"""

	poll = models.ForeignKey(Poll, verbose_name = _('Corresponding poll'))
	title = models.CharField(max_length = 400, verbose_name = ('Title'))
	text = models.TextField(verbose_name = ('text'))
	authors = models.CharField(max_length = 400, verbose_name = ('Authors'))

	def __unicode__(self):
		return self.title

	def next(self):
		"""
		Returns the next question in this Poll. This is not necessarily
		self.id += 1 since the IDs are shared across Polls.
		"""

		# TODO Check if there's a more efficient way to do this
		list = PollQuestion.objects.filter(id__gt = self.id, poll = self.poll)
		if len(list) < 1:
			return None

		return list[0]

class Vote(models.Model):
	"""
	The user votes to a question. The choice is stored as an Integerfield. The
	values yes/no/abstention correspond to the integers as follows: 0 = yes,
	1 = no, 2 = abstention.
	"""

	voting_user = models.OneToOneField(User, verbose_name = _('Voting user'))

	poll_question = models.ForeignKey(
		PollQuestion,
		verbose_name = _('Answered question'))

	choice = models.IntegerField(
		choices = ((0, _('Yes')), (1, _('No')), (2, _('Abstention'))),
		verbose_name = _('Choice'))

	def __unicode__(self):
		return '{} by #{} on {}'.format(
			self.get_choice_display(),
			self.voting_user.member_id,
			self.poll_question)