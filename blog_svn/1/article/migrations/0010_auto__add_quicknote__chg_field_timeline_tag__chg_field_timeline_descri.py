# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'QuickNote'
        db.create_table(u'article_quicknote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('note', self.gf('django.db.models.fields.TextField')(max_length=140)),
            ('post_time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'article', ['QuickNote'])


        # Changing field 'Timeline.tag'
        db.alter_column(u'article_timeline', 'tag', self.gf('django.db.models.fields.CharField')(max_length=8))

        # Changing field 'Timeline.description'
        db.alter_column(u'article_timeline', 'description', self.gf('django.db.models.fields.TextField')(max_length=140))

    def backwards(self, orm):
        # Deleting model 'QuickNote'
        db.delete_table(u'article_quicknote')


        # Changing field 'Timeline.tag'
        db.alter_column(u'article_timeline', 'tag', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Timeline.description'
        db.alter_column(u'article_timeline', 'description', self.gf('django.db.models.fields.TextField')(max_length=9999))

    models = {
        u'article.article': {
            'Meta': {'object_name': 'Article'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'labels': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['article.Label']", 'through': u"orm['article.LabelsInArticle']", 'symmetrical': 'False'}),
            'last_edit_time': ('django.db.models.fields.DateTimeField', [], {}),
            'last_view_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'markdown_content': ('django.db.models.fields.CharField', [], {'max_length': '9999'}),
            'post_time': ('django.db.models.fields.DateTimeField', [], {}),
            'raw_content': ('django.db.models.fields.CharField', [], {'max_length': '9999'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'article.label': {
            'Meta': {'object_name': 'Label'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'number_is_used': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'article.labelsinarticle': {
            'Meta': {'object_name': 'LabelsInArticle'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['article.Article']"}),
            'date_joined': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['article.Label']"})
        },
        u'article.quicknote': {
            'Meta': {'object_name': 'QuickNote'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'max_length': '140'}),
            'post_time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'article.timeline': {
            'Meta': {'object_name': 'Timeline'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '140'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        }
    }

    complete_apps = ['article']