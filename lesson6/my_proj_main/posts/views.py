from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Post

def index(request):
    return HttpResponse('Главная')


def posts_list(request):    
    posts = Post.objects.all()

    paginator = Paginator(posts, 2)
    # print(paginator.count) # Количество записей
    # print(paginator.num_pages) # Количество страниц
    # page1 = paginator.page(1)
    # print(page1)
    # print(page1.object_list)
    
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)

    context = {'page_obj': page_obj}

    return render(request, 'posts/posts_list.html', context)


def posts_detail(request, id):
    post = Post.objects.get_or_404(id = id)
    context = {'post': post}
    return render(request, 'posts/posts_detail.html', context)
