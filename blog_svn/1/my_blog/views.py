from django.shortcuts import render

from article.models import Article, Label, LabelsInArticle

from django.db.models import Count, Sum

def home(request):
	# articles = Article.objects.all().order_by('-post_time')
	page_number = request.GET.get('page')
	articles = Article.objects.get_paginated_articles(page_number)
	labels = Label.objects.render_labels()
	return render(request, 'home.html', {'articles': articles, 'labels': labels})

def about(request):
	return render(request, 'about.html')