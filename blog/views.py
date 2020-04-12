 
from django.shortcuts import render
from .models import Post
 
def index(request):
    # 取出文章中的所有内容，时间按降序排列，
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
