from django.apps import AppConfig


class BlogConfig(AppConfig):
    # 定义 app 名称 需要和应用名称一致不可以改
    name = 'blog'
    # 修改在后台显示的名称
    verbose_name = '博客'
    
