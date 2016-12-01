# coding: utf-8
from django.db import models
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# 标签控制类
class LabelManager(models.Manager):
	# render出不同大小的label，用于前台的展示
	def render_labels(self):
		# 获取所有标签和每个标签引用次数
		# labels = self.all().annotate(total_used_number=Sum('labelsinarticle__label__number_is_used')).order_by('-total_used_number')
		labels = Label.objects.annotate(num_articles=Count('article')).order_by('-num_articles')[:40]
		# 所有标签引用次数
		# total_used = LabelsInArticle.objects.all().count()
		total_label_used = float(LabelsInArticle.objects.all().count()) / (labels.count() + 1)
		for label in labels:
			label.size = label.num_articles / total_label_used * 100
			# 做微调
			if label.size > 200:
				label.size = 200
			elif label.size < 80:
				label.size = 80
		return labels

# 博文控制类
class ArticleManager(models.Manager):
	def get_articles_by_label(self, label):
		return self.filter(labelsinarticle__label=label)

	# 内部使用，用来分页博文
	def paginate_articles(self, all_articles, page_number):
		paginator = Paginator(all_articles, 5)
		p_range = paginator.page_range
		range_len = len(p_range)
		if page_number:
			page_number = int(page_number)
		if range_len <= 10:
			pass
		elif page_number <= 5:
			p_range = range(1, 11)
		elif page_number >= range_len - 5:
			p_range = range(page_number - 4, range_len + 1)
		else:
			p_range = range(page_number - 4, page_number + 6)

		paginator.p_range = p_range
		try:
			articles = paginator.page(page_number)
		except PageNotAnInteger:
			articles = paginator.page(1)
		except EmptyPage:
			articles = paginator.page(paginator.num_pages)
		if not page_number:
			articles.page_number = 1
		else:
			articles.page_number = int(page_number)
		return articles

	# 获取所有分页过的文章
	def get_paginated_articles(self, page_number):
		all_articles = self.all().order_by('-post_time')
		return self.paginate_articles(all_articles, page_number)

	# 根据具体标签获取分页过的文章
	def get_paginated_articles_by_label(self, label, page_number):
		all_articles_by_label = self.filter(labelsinarticle__label=label).order_by('-post_time')
		return self.paginate_articles(all_articles_by_label, page_number)

# 标签
class Label(models.Model):
	name = models.CharField(max_length=100, verbose_name='标签名')
	number_is_used = models.IntegerField(verbose_name='被引用次数', default=1) #暂时使用这个常量来计数
	objects = LabelManager()

	def __unicode__(self):
		return self.name
	
# 博文
class Article(models.Model):
	title = models.CharField(max_length=100, verbose_name='标题')
	raw_content = models.TextField(max_length=9999, verbose_name='原始博文')
	markdown_content = models.TextField(max_length=9999, verbose_name='转义博文')
	post_time = models.DateTimeField(verbose_name='发布日期')
	last_edit_time = models.DateTimeField(verbose_name='最后编辑日期')
	last_view_time = models.DateTimeField(auto_now=True, verbose_name='最后浏览日期')
	labels = models.ManyToManyField(Label, through='LabelsInArticle')
	objects = ArticleManager()

	def __unicode__(self):
		return self.title

class LabelsInArticle(models.Model):
    article = models.ForeignKey(Article)
    label = models.ForeignKey(Label)
    date_joined = models.DateField(auto_now=True)

    def __unicode__(self):
		return self.article.title + ' - ' + self.label.name

# 时间线
class Timeline(models.Model):
	date = models.DateField()
	tag = models.CharField(max_length=16, verbose_name='标签')
	description = models.TextField(max_length=140, verbose_name='描述')
	user = models.IntegerField(default=0)

	def __unicode__(self):
		return str(self.date) + ' - ' + self.tag + ' - ' + self.description

# 随手记
class QuickNote(models.Model):
	note = models.TextField(max_length=140, verbose_name='内容')
	post_time = models.DateTimeField(verbose_name='发布时间')

	def __unicode__(self):
		return self.note	

