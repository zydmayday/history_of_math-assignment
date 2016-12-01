# coding: utf-8
from django.shortcuts import render

# Create your views here.
# 获取从豆瓣返回的值，code
def callback(request):
	code_id = request.GET.get('code')
	return render(request, 'spider.html', {'code_id': code_id})