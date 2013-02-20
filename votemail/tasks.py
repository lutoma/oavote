# coding: utf-8

from django.core.mail import EmailMessage, send_mass_mail
from django.template.loader import get_template, Context
from django.utils.translation import ugettext as _
	
def send_token_mails(users):
	"""
	Sends emails containing the voting token to one or more users.
	"""

	mails = []

	for user in users:
		print('Formatting mail to {}'.format(user.email_address))

		# Format mail and store it
		mail_template = get_template('votemail/mails/token.txt')
		message = mail_template.render(Context({'user': user}))
		subject = _(u'Your voting token for the "{}" poll').format(user.poll.title)
		mail_to = (u'{} <{}>'.format(user.first_name, user.email_address),)

		mails.append((subject, message, None, mail_to))

	print('Sending mails')
	send_mass_mail(mails, fail_silently = False)
	users.update(mail_sent = True)
