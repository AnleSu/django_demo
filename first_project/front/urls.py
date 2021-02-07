from django.urls import path
from . import views

# 应用命名空间
app_name = 'front'

urlpatterns = [
    path('', views.index),
    path('login/', views.login),
    # url 命名
    path('signin/', views.login, name='login'),
    path('index2/', views.index2),
    path('index3/', views.index3)
]