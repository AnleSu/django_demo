from django.shortcuts import render
from .models import Category,Article
from frontuser.models import FrontUser
from django.http import HttpResponse
# Create your views here.

def index(request):
    # article = Article(title='abc',content='qwertyuio')
    # category = Category(name='最新文章')
    # category.save()
    # article.category = category
    # article.save()

    article = Article.objects.first()
    print(article.category.name)
    return HttpResponse('success')

def delete_view(request):
    category = Category.objects.get(pk=1)
    category.delete()
    return HttpResponse('success')

def one_to_many_view(request):
    # 一对多关联操作
    # article = Article(title='钢铁是怎么样炼成的',content='good')
    # category = Category.objects.first()
    # author = FrontUser.objects.first()
    # article.category = category
    # article.author = author
    # article.save()
    # return HttpResponse('success')

    # # 获取某个分类下所有的文章
    category = Category.objects.first()
    # # django自动生成的
    #
    # articles = category.article_set.all()
    # # 修改related_name
    # # articles = category.articles.all()
    # # category.article_set.first()
    # # category.article_set.filter()
    # for article in articles:
    #     print(article)

    article = Article(title='aaa',content='ccc')
    article.author = FrontUser.objects.first()
    # article.save()
    # category_id 可以为空才可以用这种方式
    # bulk=False 自动执行article.save() 如果不加需要手动执行article.save()
    category.articles.add(article, bulk=False)
    category.save()
    return HttpResponse('success')