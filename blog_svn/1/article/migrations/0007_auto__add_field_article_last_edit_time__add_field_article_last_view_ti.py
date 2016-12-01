# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Article.last_edit_time'
        db.add_column(u'article_article', 'last_edit_time',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 9, 10, 0, 0)),
                      keep_default=False)

        # Adding field 'Article.last_view_time'
        db.add_column(u'article_article', 'last_view_time',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 9, 10, 0, 0), blank=True),
                      keep_default=False)


        # Changing field 'Article.post_time'
        db.alter_column(u'article_article', 'post_time', self.gf('django.db.models.fields.DateTimeField')())

    def backwards(self, orm):
        # Deleting field 'Article.last_edit_time'
        db.delete_column(u'article_article', 'last_edit_time')

        # Deleting field 'Article.last_view_time'
        db.delete_column(u'article_article', 'last_view_time')


        # Changing field 'Article.post_time'
        db.alter_column(u'article_article', 'post_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

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
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'view_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
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
        }
    }

    complete_apps = ['article']