# coding: utf-8
from django.db import models

# class HistoryManager(models.Manager):


class History(models.Model):
	date = models.DateField(verbose_name='发生日期')
	title = models.CharField(max_length=100, verbose_name='时间标题')
	event = models.TextField(max_length=1000, verbose_name='事件')
	post_time = models.DateTimeField(auto_now=True, verbose_name='发布日期')
	# objects = HistoryManager()

	def __unicode__(self):
		return self.title