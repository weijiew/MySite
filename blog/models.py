from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    # 标题
    title = models.CharField(max_length=70)
    # 内容
    body = models.TextField()
    # 创建时间
    created_time = models.DateTimeField()
    # 修改时间
    modified_time = models.DateTimeField()
    # 摘要 blank = True 表示可以为空，CharField 默认不为空
    excerpt = models.CharField(max_length=200, blank=True)
    # 分类关系 一篇文章只能有一个类别，删除这个类的话，关于这个类的所有文章都需要删除，也就是级联删除
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # 标签关系 允许标签为空，并且一个标签下有多篇文章，一篇文章对应多个标签
    tag = models.ManyToManyField(Tag, blank=True)
    # 作者和用户间的关系。
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title