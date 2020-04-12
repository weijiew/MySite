from django.urls import path
 
from . import views

# 视图函数命名空间：告诉 django 这个 urls 模块属于 blog，防止和别的应用弄混
app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:pk>/', views.detail, name='detail'),
]