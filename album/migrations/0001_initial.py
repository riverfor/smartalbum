# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'album_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('twitter_username', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('skip_flag', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'album', ['User'])

        # Adding model 'Photo'
        db.create_table(u'album_photo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['album.User'])),
            ('tweet_id', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('tweet_url', self.gf('django.db.models.fields.TextField')()),
            ('expend_url', self.gf('django.db.models.fields.TextField')()),
            ('save_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'album', ['Photo'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'album_user')

        # Deleting model 'Photo'
        db.delete_table(u'album_photo')


    models = {
        u'album.photo': {
            'Meta': {'object_name': 'Photo'},
            'expend_url': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'save_date': ('django.db.models.fields.DateTimeField', [], {}),
            'tweet_id': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'tweet_url': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['album.User']"})
        },
        u'album.user': {
            'Meta': {'object_name': 'User'},
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'skip_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'twitter_username': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['album']