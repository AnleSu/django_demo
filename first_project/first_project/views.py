from django.shortcuts import render
from django.http import HttpResponse
class Person(object):
    def __init__(self, username):
        self.username = username


def prjectIndex(request):
    p = Person('zhangsan')
    context = {
        'username': "xiaoming",
        'person': p,
        'personDic': {
            'username': 'hhh'

        },
        'persons': [
            'aaaa',
            'bbbbb'
        ]
    }
    return render(request, 'index.html', context=context)

def projectIndex2(request):
    context = {
        'age': 16
    }
    return render(request, 'index.html', context=context)

def projectIndex3(request):
    context = {
        'heros': [
            '鲁班',
            '项羽',
            '程咬金'
        ],
        'person': {
            'username': 'hhh',
            'age': 18,
            'height': 65
        },
        'books': [
            {
                'name':'三国',
                'author':'罗贯中',
                'price':99
            },
            {
                'name': '水浒',
                'author': '施耐庵',
                'price': 109
            },
            {
                'name': '西游',
                'author': '吴承恩',
                'price': 199
            },
            {
                'name': '红楼',
                'author': '曹雪芹',
                'price': 129
            },

        ],
        'comments':[
            # 'good',
            # 'best'
        ]
    }
    return render(request, 'index.html', context=context)
def login(request):
    next = request.GET.get('next')
    text = '登录完成要跳转的页面是 %s' % next
    return HttpResponse(text)

def book(request):
    return HttpResponse('读书页面')
def book_detail(request, book_id, category):
    text = '图书ID是：%s 分类：%s' % (book_id,category)
    return HttpResponse(text)
def movie(request):
    return HttpResponse('电影页面')

def city(request):
    return HttpResponse('同城页面')
