from django.contrib import admin
from .models import Post, Category, Tag

#  后台显示更详细的文章信息
class PostAdmin(admin.ModelAdmin):
    # 显示信息的维度
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    # 简化新增文章的配置，将手动设置时间改为自动设置！
    fields = ['title', 'body', 'excerpt', 'category', 'tags']
    # 重写次方法，实现了将文章作者和登陆后台的人相关联，也就是登陆的人就是作者
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

# 注册写好的模型也就是 models.py 文件中写好的类名
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)