 
from django.shortcuts import render
 
def index(request):
    return render(request, 'blog/index.html', context={
        'title': '我的博客',
        'welcome': '欢迎访问我的博客'
        })