# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Article.markdown_content'
        db.alter_column(u'article_article', 'markdown_content', self.gf('django.db.models.fields.TextField')(max_length=9999))

        # Changing field 'Article.raw_content'
        db.alter_column(u'article_article', 'raw_content', self.gf('django.db.models.fields.TextField')(max_length=9999))

    def backwards(self, orm):

        # Changing field 'Article.markdown_content'
        db.alter_column(u'article_article', 'markdown_content', self.gf('django.db.models.fields.CharField')(max_length=9999))

        # Changing field 'Article.raw_content'
        db.alter_column(u'article_article', 'raw_content', self.gf('django.db.models.fields.CharField')(max_length=9999))

    models = {
        u'article.article': {
            'Meta': {'object_name': 'Article'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'labels': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['article.Label']", 'through': u"orm['article.LabelsInArticle']", 'symmetrical': 'False'}),
            'last_edit_time': ('django.db.models.fields.DateTimeField', [], {}),
            'last_view_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'markdown_content': ('django.db.models.fields.TextField', [], {'max_length': '9999'}),
            'post_time': ('django.db.models.fields.DateTimeField', [], {}),
            'raw_content': ('django.db.models.fields.TextField', [], {'max_length': '9999'}),
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