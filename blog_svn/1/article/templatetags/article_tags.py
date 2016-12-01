# coding: utf-8
from django import template
import calendar
import time, datetime

register = template.Library()

@register.filter(expects_localtime=True)
def render_date(post_time):
	SEC = 60
	MIN = 60
	HOU = 24
	today_format = '%H:%M'
	date_format = '%Y %m月%d日 %H:%M'
	now_timestamp = time.time()
	post_time_timestamp = time.mktime(post_time.timetuple())
	timestamp_delta = now_timestamp - post_time_timestamp
	if timestamp_delta < SEC:
		return str(int(timestamp_delta)) + '秒前'
	elif timestamp_delta < SEC * MIN:
		return str(int(timestamp_delta / SEC)) + '分钟前'
	elif datetime.datetime.today().day == post_time.day:
		return '今天 ' + post_time.strftime(today_format)
	else:
		return post_time.strftime(date_format)

register.filter('render_date', render_date)