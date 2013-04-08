# coding: utf-8

from django.utils.translation import ugettext_lazy as _
from vote.models import User, Poll, PollQuestion, Vote
from django.contrib import admin

class PollAdmin(admin.ModelAdmin):
	list_display = ('title', 'active')
	list_filter = ['active']

class PollQuestionAdmin(admin.ModelAdmin):
	list_display = ('title', 'authors', 'get_result')
	list_filter = ['poll']

class VoteAdmin(admin.ModelAdmin):
	list_display = ('voting_user', 'poll_question', 'choice')
	list_filter = ['poll_question']

admin.site.register(User)
admin.site.register(Poll, PollAdmin)
admin.site.register(PollQuestion, PollQuestionAdmin)
admin.site.register(Vote, VoteAdmin)