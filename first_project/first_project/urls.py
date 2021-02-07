"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from book import views
from django.http import HttpResponse
from django.urls import path,include
from . import views

def index(request):
    return HttpResponse('HOME')

urlpatterns = [
    # path('admin/', admin.site.urls),
    # http://127.0.0.1:9000/ 默认页面
    # path('', index),
    # path('book/', views.book),
    # # 参数名book_id 必须和视图函数中的参数名保持一致
    # path('book/detail/<book_id>/<category_id>', views.book_detail),
    # path('book/author/', views.author_detail),

    # url 命名
    path('', include('front.urls')),
    path('cms/', include('cms.urls')),
    path('project/index/', views.prjectIndex),
    path('project/index2/', views.projectIndex2),
    path('project/index3/', views.projectIndex3),
    path('book/', views.book, name='book'),
    path('book/detail/<book_id>/<category>', views.book_detail, name='book_detail'),
    path('movie/', views.movie, name='movie'),
    path('city/', views.city, name='city'),
    path('login/', views.login, name='login')

]
