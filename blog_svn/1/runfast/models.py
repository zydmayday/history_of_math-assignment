# coding: utf-8
from django.db import models

# Create your models here.

class RunFast(models.Model):
	name = models.CharField(max_length=100, verbose_name='名称')
	time = models.DateTimeField(verbose_name='游戏时间')
	winner = models.CharField(max_length=100, verbose_name='胜者')

	def __unicode__(self):
		return self.name

