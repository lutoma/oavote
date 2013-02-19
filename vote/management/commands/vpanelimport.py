# coding: utf-8

from django.core.management.base import BaseCommand, CommandError
from django.utils.translation import ugettext as _
from vote.models import Poll, User
import csv

class Command(BaseCommand):
	"""
	Imports users that are allowed to vote in a poll from an vPanel export CSV
	file with the fields 'Mitgliedsnummer', 'Vorname', 'E-Mail'.
	"""

	args = '<poll_id> <csv_file>'
	help = 'Imports users allowed to vote from a VPanel CSV file'

	def handle(self, *args, **options):
		# Check for sane command line arguments
		try:
			if len(args) < 2:
				raise ValueError

			poll_id = int(args[0])
		except ValueError:
			raise CommandError(_('Usage: {}').format(self.args))

		# Try to find poll by ID
		try:
			poll = Poll.objects.get(pk=int(poll_id))
		except Poll.DoesNotExist:
			raise CommandError(_('Poll #{} does not exist').format(poll_id))

		# Now actually read stuff
		with open(args[1], 'rb') as csv_file:
			reader = csv.reader(csv_file, delimiter=',', quotechar='"')

			# Check if the first row is correct. If it is, it should contain the
			# Name of the needed exported fields, which are 'Mitgliedsnummer',
			# 'Vorname', 'E-Mail'
			if(reader.next() != ['Mitgliedsnummer','Vorname','E-Mail']):
				raise CommandError(_('Invalid CSV file. Please see Readme.'))

			for row in reader:
				new_user = User(poll = poll, used = False, mail_sent = False)

				new_user.email_address = row[2]
				new_user.first_name = row[1]
				new_user.member_id = row[0]

				new_user.save()
				self.stdout.write(_('Imported user #{}').format(row[0]))
