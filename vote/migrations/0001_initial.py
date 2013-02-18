# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Poll'
        db.create_table('vote_poll', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('vote', ['Poll'])

        # Adding model 'User'
        db.create_table('vote_user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('poll', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vote.Poll'])),
            ('used', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('mail_sent', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('email_address', self.gf('django.db.models.fields.EmailField')(max_length=254)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('member_id', self.gf('django.db.models.fields.IntegerField')()),
            ('token', self.gf('django.db.models.fields.CharField')(default='5e676fa1-cc86-41b1-881e-49f434294187', max_length=36)),
            ('voting_ip', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39, null=True, blank=True)),
        ))
        db.send_create_signal('vote', ['User'])

        # Adding model 'PollQuestion'
        db.create_table('vote_pollquestion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('poll', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vote.Poll'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('authors', self.gf('django.db.models.fields.CharField')(max_length=400)),
        ))
        db.send_create_signal('vote', ['PollQuestion'])

        # Adding model 'Vote'
        db.create_table('vote_vote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('voting_user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['vote.User'], unique=True)),
            ('poll_question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vote.PollQuestion'])),
            ('choice', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('vote', ['Vote'])


    def backwards(self, orm):
        # Deleting model 'Poll'
        db.delete_table('vote_poll')

        # Deleting model 'User'
        db.delete_table('vote_user')

        # Deleting model 'PollQuestion'
        db.delete_table('vote_pollquestion')

        # Deleting model 'Vote'
        db.delete_table('vote_vote')


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
            'token': ('django.db.models.fields.CharField', [], {'default': "'7a96c8a4-6191-43ec-ac4f-2a313d400396'", 'max_length': '36'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'voting_ip': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39', 'null': 'True', 'blank': 'True'})
        },
        'vote.vote': {
            'Meta': {'object_name': 'Vote'},
            'choice': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poll_question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vote.PollQuestion']"}),
            'voting_user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['vote.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['vote']