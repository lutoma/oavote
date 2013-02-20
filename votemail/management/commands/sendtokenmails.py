# coding: utf-8

from django.core.management.base import BaseCommand, CommandError
from django.utils.translation import ugettext as _
from vote.models import Poll, User
from votemail.tasks import send_token_mails

class Command(BaseCommand):
	"""
	Sends emails with token to all Users of a Poll.
	"""

	args = '<poll_id>'
	help = 'Sends emails with token to all Users of a Poll.'

	def handle(self, *args, **options):
		# Check for sane command line arguments
		try:
			if len(args) < 1:
				raise ValueError

			poll_id = int(args[0])
		except ValueError:
			raise CommandError(_('Usage: {}').format(self.args))

		# Try to find poll by ID
		try:
			poll = Poll.objects.get(pk=int(poll_id))
		except Poll.DoesNotExist:
			raise CommandError(_('Poll #{} does not exist').format(poll_id))

		send_token_mails(User.objects.filter(poll = poll, mail_sent = False))
