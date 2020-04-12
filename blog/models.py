from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    # 配置后台中文名称
    class Meta:
        verbose_name = '分类'
        # 当存在多篇文章时为复数，这里中文还是原名
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField('标题', max_length=70)
    body = models.TextField('正文')
    # 自动填充当前时间
    created_time = models.DateTimeField('创建时间',default=timezone.now)
    modified_time = models.DateTimeField('修改时间')
    excerpt = models.CharField('摘要', max_length=200, blank=True)
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
    
    # 设置默认保存修改时间
    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        
    def __str__(self):
        return self.title