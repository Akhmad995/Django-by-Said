from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
from .models import Post
from .models import User

def index(request):
    return HttpResponse('Главная')


def posts_list(request):
    # CRUD

    # получение записи по первичному ключу
    user = User.objects.get(pk=1)
    
    # Создание записи
    # post = Post.objects.get_or_create(title='Заголовок 3', text='Длинный текст 3', author=user)
    post = Post.objects.get(id=3)

    # Обновление
    post.text = 'Длинный текст 4 - обновление'
    post.save()

    # Удаление
    # post.delete()
    
    # Получаем список записей
    posts = Post.objects.all()

    # Получение части публикаций
    # posts = Post.objects.exclude(title='Название заголовка')

    # Метод filter
    # posts = Post.objects.filter(title='Название заголовка')
    # posts = Post.objects.filter(author=user)
    
    # contains - содержит подстроку
    # posts = Post.objects.filter(text_contains='обнов')
    # startwith, endwith - поле начинается*заканчивается
    
    # in - вхождение в набор значений 
    # posts = Post.objects.filter(title_in=('Заг1', 'Заг2'))

    # range - вхождение в диапозон/интервал
    # posts = Post.objects.filter(id_range=(1, 5))

    context = {'current_id': 5, 'form': PostForm, 'posts': posts}
    return render(request, 'posts/posts_list.html', context)


def posts_detail(request, id):
    post = Post.objects.get_or_404(id = id)
    context = {'post': post}
    return render(request, 'posts/posts_detail.html', context)
