from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # on_delete 表示当Category表中删除了某条数据后，Article中引用Category中该条数据的数据 如何处理
    # 就是Category对Article的影响
    # CASCADE 级联删除
    # related_name 修改关联名字（就是category_set的名字） 修改了就调用不到category_set 需要用 articles调用
    category = models.ForeignKey("Category",on_delete=models.CASCADE, related_name='articles')

    # 引用不同app中的模型
    author = models.ForeignKey('frontuser.FrontUser',on_delete=models.CASCADE, null=True)
    def __str__(self):
        return '<Article: (id:%s, title:%s)>' % (self.id, self.title)

class Comment(models.Model):
    content = models.TextField()

    # 两种方式 引用自身
    # origin_content = models.ForeignKey('self', on_delete=models.CASCADE)
    origin_content = models.ForeignKey('Comment', on_delete=models.CASCADE)