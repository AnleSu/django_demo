from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, reverse  # 重定向,反转
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    # 如果没有传递 ?username=xxx 就跳转登录
    username = request.GET.get('username')
    if username:
        return HttpResponse("Front home")
    else:
        # return redirect('/login/')
        # 重命名:login  命名空间：front
        print('='*30)
        login_url = reverse('front:login')
        print(login_url)
        print('=' * 30)
        return redirect(login_url)

def login(request):
    return HttpResponse('Front Login')

def index2(request):
    html = render_to_string("index.html")
    return HttpResponse(html)

def index3(request):
    return render(request, 'index.html')