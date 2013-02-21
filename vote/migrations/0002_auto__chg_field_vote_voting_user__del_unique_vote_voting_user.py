# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Vote', fields ['voting_user']
        db.delete_unique('vote_vote', ['voting_user_id'])


        # Changing field 'Vote.voting_user'
        db.alter_column('vote_vote', 'voting_user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vote.User']))

    def backwards(self, orm):

        # Changing field 'Vote.voting_user'
        db.alter_column('vote_vote', 'voting_user_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['vote.User'], unique=True))
        # Adding unique constraint on 'Vote', fields ['voting_user']
        db.create_unique('vote_vote', ['voting_user_id'])


    models = {
        'vote.poll': {
            'Meta': {'object_name': 'Poll'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        },
        'vote.pollquestion': {
            'Meta': {'object_name': 'PollQuestion'},
            'authors': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poll': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vote.Poll']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        },
        'vote.user': {
            'Meta': {'object_name': 'User'},
            'email_address': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mail_sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'member_id': ('django.db.models.fields.IntegerField', [], {}),
            'poll': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vote.Poll']"}),
            'token': ('django.db.models.fields.CharField', [], {'default': "'a05174d8-234d-4ffa-b490-dac45ab61736'", 'max_length': '36'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'voting_ip': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39', 'null': 'True', 'blank': 'True'})
        },
        'vote.vote': {
            'Meta': {'object_name': 'Vote'},
            'choice': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poll_question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vote.PollQuestion']"}),
            'voting_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vote.User']"})
        }
    }

    complete_apps = ['vote']