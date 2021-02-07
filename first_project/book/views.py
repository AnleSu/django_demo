from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# 视图函数的第一个参数必须是request
# 返回值必须是HttpResponseBase的子类的对象
def book(request):
    return HttpResponse('图书首页')

def book_detail(request,book_id,category_id):
    text = 'book id is %s ,book category is %s' % (book_id, category_id)
    return HttpResponse(text)

# 问号形式拼接的参数（查询字符串的方式）
def author_detail(request):
    # GET请求 所以通过request.GET来获取参数  类似于字典
    author_id = request.GET.get('id') # author_id = request.GET['id'] 两种写法
    text = 'author id is %s' % author_id
    return HttpResponse(text)