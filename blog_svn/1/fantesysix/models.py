# coding: utf-8
from django.db import models

# Create your models here.
class History(models.Model):
	guest_card = models.CharField(max_length=9999, verbose_name='玩家手牌')
	own_card = models.CharField(max_length=9999, verbose_name='程序手牌')
	guest_score = models.IntegerField(verbose_name='玩家得分')
	own_score = models.CharField(max_length=9999, verbose_name='程序得分')
	time = models.DateTimeField(verbose_name='时间', auto_now=True)

class Hypothesis(models.Model):
	hypothesis = models.CharField(max_length=9999, verbose_name='参数')
	time = models.DateTimeField(verbose_name='时间', auto_now=True)

class HistoryDealCards(models.Model):
	deal_cards = models.CharField(max_length=9999, verbose_name='历史牌组')
	time = models.DateTimeField(verbose_name='时间', auto_now=True)
