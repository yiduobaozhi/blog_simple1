from django.shortcuts import render
#coding:utf-8
from django.http import HttpResponseRedirect
from . import models

def index(request):
    articles=models.Article.objects.all()
    return render(request,'index.html',{'articles':articles})

def page_article(request,article_id):
    article=models.Article.objects.get(pk=article_id)
    return render(request,'page_article.html',{'article':article})

def edit_page(request,article_id):
    if str(article_id) == '0':
        return render(request, 'edit_page.html')
    article=models.Article.objects.get(pk=article_id)
    return render(request,'edit_page.html',{'article':article})


def edit_action(request):
    title=request.POST.get('title','TITLE')        # 获取前端表单传过来的数据
    content=request.POST.get('content','CONTENT')
    article_id=request.POST.get('article_id','0')
    if article_id=='0':
        models.Article.objects.create(title=title,content=content)
        return HttpResponseRedirect('/index/')       # 重定向
    article=models.Article.objects.get(pk=article_id)
    article.title=title
    article.content=content
    article.save()
    return render(request,'page_article.html',{'article':article})