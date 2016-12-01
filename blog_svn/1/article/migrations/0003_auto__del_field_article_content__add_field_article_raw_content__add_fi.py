# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Article.content'
        db.delete_column(u'article_article', 'content')

        # Adding field 'Article.raw_content'
        db.add_column(u'article_article', 'raw_content',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=9999),
                      keep_default=False)

        # Adding field 'Article.markdown_content'
        db.add_column(u'article_article', 'markdown_content',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=9999),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Article.content'
        raise RuntimeError("Cannot reverse this migration. 'Article.content' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Article.content'
        db.add_column(u'article_article', 'content',
                      self.gf('django.db.models.fields.CharField')(max_length=9999),
                      keep_default=False)

        # Deleting field 'Article.raw_content'
        db.delete_column(u'article_article', 'raw_content')

        # Deleting field 'Article.markdown_content'
        db.delete_column(u'article_article', 'markdown_content')


    models = {
        u'article.article': {
            'Meta': {'object_name': 'Article'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'labels': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['article.Label']", 'through': u"orm['article.LabelsInArticle']", 'symmetrical': 'False'}),
            'markdown_content': ('django.db.models.fields.CharField', [], {'max_length': '9999'}),
            'post_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'raw_content': ('django.db.models.fields.CharField', [], {'max_length': '9999'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'article.label': {
            'Meta': {'object_name': 'Label'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'number_is_used': ('django.db.models.fields.IntegerField', [], {'default': '0'})
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