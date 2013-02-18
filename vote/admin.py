# coding: utf-8

from django.utils.translation import ugettext_lazy as _
from vote.models import User, Poll, PollQuestion, Vote
from django.contrib import admin

admin.site.register(User)
admin.site.register(Poll)
admin.site.register(PollQuestion)
admin.site.register(Vote)