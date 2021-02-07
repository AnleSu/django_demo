from django.shortcuts import render
from datetime import datetime
def index(request):
    context = {
        'greet': greet,
        'username': 'liming'
    }
    return render(request,'index.html',context=context)

def greet(word):
    return "hello world %s" % word


def add_view(request):
    context = {
        'value1': ['1','2','3'],
        'value2': ['4','5','6']
    }
    return render(request,'add.html',context=context)

def cut_view(request):
    return render(request,'cut.html')

def date_view(request):
    context = {
        'today':datetime.now()
    }
    return render(request,'date.html',context=context)

def company(request):
    pass

def school(request):
    pass