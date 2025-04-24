from django.shortcuts import redirect
from django.shortcuts import render
from blog.models import Post

def index(request):
        recent_posts = Post.objects.order_by('-created_at')[:3]
        return render(request, 'index.html', {'recent_posts': recent_posts})