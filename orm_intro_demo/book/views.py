import pytz
from django.shortcuts import render
from .models import Book
from django.http import HttpResponse
from .models import Article,Person
from datetime import datetime,timedelta
# Create your views here.

def index(request):
    # book = Book(name='西游',author='吴承恩',price=100)
    # book.save()

    # pk primary key的简写  只针对于主键是id的情况
    # book = Book.objects.get(pk=1)


    # filter 返回一个列表 即使只有一条数据也是列表
    # books = Book.objects.filter(name='西游').first()
    # print(books)

    # book = Book.objects.get(pk=1)
    # book.delete()

    book = Book.objects.get(pk=2)
    book.price = 333
    book.save()
    return HttpResponse("图书添加成功")

def articleIndex(request):
    # article = Article(removed=False)

    #
    article = Article()
    article.title = '111'
    article.save()

    # now = datetime.now()
    # utc_timezone = pytz.timezone("UTC")
    # utc_now = now.astimezone(utc_timezone)


    return HttpResponse("success")

def email_view(request):
    p = Person(email='xxx')
    p.save()
    return HttpResponse("success")