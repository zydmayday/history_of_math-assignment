# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils import timezone
import json
import datetime

from article.models import Article, Label, LabelsInArticle, Timeline, QuickNote
# Create your views here.

# 获取所有文章
def articles(request):
	articles = Article.objects.all()
	return render(request, 'articles.html', {'articles': articles})

# 获取特定文章
def article(request, article_id):
	article = Article.objects.get(id=article_id)
	labels = Label.objects.render_labels()
	return render(request, 'article.html', {'article': article, 'labels': labels})

# 获取特定标签下的所有文章
def label(request, label_id):
	label = Label.objects.get(id=label_id)
	labels = Label.objects.render_labels()
	page_number = request.GET.get('page')
	articles = Article.objects.get_paginated_articles_by_label(label, page_number)
	return render(request, 'articles_for_label.html', {'articles': articles, 'label': label, 'labels': labels})

# 添加文章
def add_article(request):
	if request.method == 'GET':
		labels = Label.objects.all()
		return render(request, 'add_article.html', {'labels': labels})
	elif request.method == 'POST':
		article_title = request.POST['article_title']
		article_raw_content = request.POST['article_raw_content']
		article_markdown_content = request.POST['article_markdown_content']
		labels = request.POST.getlist('labels[]')
		new_article = Article.objects.create(title=article_title, raw_content=article_raw_content, markdown_content=article_markdown_content, post_time=timezone.now(), last_edit_time=timezone.now())
		for label_id in labels:
			label = Label.objects.get(id=label_id)
			# label.number_is_used = label.number_is_used + 1
			label.save()
			lia = LabelsInArticle(article=new_article, label=label)
			lia.save()
		return render(request, 'add_article_form.html', {})

def edit_article_list(request):
	articles = Article.objects.all()
	return render(request, 'edit_article_list.html', {'articles': articles})

# 编辑文章
def edit_article(request, article_id):
	if request.method == 'GET':
		article = Article.objects.get(id=article_id)
		labels_in_article = article.labels.all()
		labels = Label.objects.all()
		return render(request, 'edit_article.html', {'article': article, 'labels': labels, 'labels_in_article': labels_in_article})
	elif request.method == 'POST':
		edit_article = Article.objects.get(id=article_id)
		edit_article.title = request.POST['article_title']
		edit_article.raw_content = request.POST['article_raw_content']
		edit_article.markdown_content = request.POST['article_markdown_content']
		edit_article.last_edit_time = timezone.now()
		edit_article.save()
		# 清楚所有关联label
		edit_article.labels.clear()
		# 重新绑定
		labels = request.POST.getlist('labels[]')
		for label_id in labels:
			label = Label.objects.get(id=label_id)
			# label.number_is_used = label.number_is_used + 1
			label.save()
			lia = LabelsInArticle(article=edit_article, label=label)
			lia.save()
		labels = Label.objects.all()
		labels_in_article = edit_article.labels.all()
		return render(request, 'edit_article_form.html', {'article': edit_article, 'labels': labels, 'labels_in_article': labels_in_article})

# 添加标签
def add_label(request):
	label_name = request.POST['label_name']
	new_label, created = Label.objects.get_or_create(name=label_name);
	label = {}
	label['id'] = new_label.id
	label['name'] = label_name
	label['created'] = created
	return HttpResponse(json.dumps(label), content_type="application/json")


# 获取所有的timeline
def get_timelines(request):
	timelines_for_zyd = Timeline.objects.filter(user = 0).order_by('date')
	timelines_for_lh = Timeline.objects.filter(user = 1).order_by('date')
	return render(request, 'timeline.html', {'timelines_for_zyd': timelines_for_zyd,'timelines_for_lh': timelines_for_lh})

# 添加时间线
def add_timeline(request):
	if request.method == 'GET':
		return render(request, 'add_timeline.html', {})
	elif request.method == 'POST':
		timeline_date = request.POST['timeline_date']
		timeline_tag = request.POST['timeline_tag']
		timeline_description = request.POST['timeline_description']
		date = timeline_date.split('-')
		# print date
		Timeline(date=datetime.date(int(date[0]), int(date[1]), int(date[2])), tag=timeline_tag, description=timeline_description).save()
		return render(request, 'add_timeline_form.html', {})

# 获取随手记
def get_quicknotes(request):
	quicknotes = QuickNote.objects.all().order_by('-post_time')[:10]
	return render(request, 'quicknote.html', {'quicknotes': quicknotes, 'last_id': 11})

def get_quicknotes_by_ajax(request, quicknote_id):
	start = int(quicknote_id)
	end = start + 5
	quicknotes = QuickNote.objects.all().order_by('-post_time')[start : end]
	return render(request, 'quicknote_list.html', {'quicknotes': quicknotes, 'last_id': end+1})

