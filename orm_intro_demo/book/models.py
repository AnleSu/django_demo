from django.db import models

# Create your models here.
# 将一个普通类变成一个可以映射到数据库中orm模型 必须将父类设置为models.Model
class Book(models.Model):
    # AutoField  Int类型   自增长
    id = models.AutoField(primary_key=True)
    # varchar(100) 不为空
    name = models.CharField(max_length=100,null=False)
    author = models.CharField(max_length=100,null=False)
    price = models.FloatField(null=False,default=0)

    # 格式化对象的打印
    def __str__(self):
        return "<Book:({name},{author},{price})>".format(name=self.name,author=self.author,price=self.price)
    # 1.python manage.py makemigrations
    # 2.python manage.py migrate


class Publisher(models.Model):
    # 没设置主键会自定生成一个名叫id的主键
    name = models.CharField(max_length=100,null=False)
    address = models.CharField(max_length=100,null=False)

class Article(models.Model):
    # BigAutoField  64位Int类型 自增长

    # 自定义的field作为主键 必须设置primary_key=True
    id = models.BigAutoField(primary_key=True)
    #没指定null=False默认就是False 不能为空
    removed = models.BooleanField(default=False)
    # 使用CharField 需要指定max_length
    # 超过254个字符 不建议使用 可使用TextField
    title = models.CharField(max_length=200,null=True)
    # auto_now 每次调用save方法的时候会调用当前时间更新
    # auto_now_add: 第一次添加数据时获取当前时间更新
    creat_time = models.DateTimeField(auto_now=True)

class Person(models.Model):
    # EmailField不会验证插入的数据是否符合email的格式  以后使用ModelForm的时候会起作用
    email = models.EmailField()
    sign = models.TextField()