from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):
    return HttpResponse('Главная')


def posts_list(request):    
    posts = Post.objects.all()

    context = {'posts': posts}
    return render(request, 'posts/posts_list.html', context)


def posts_detail(request, id):
    post = Post.objects.get_or_404(id = id)
    context = {'post': post}
    return render(request, 'posts/posts_detail.html', context)
