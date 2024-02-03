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
    # posts = Post.objects.filter(text__contains='обнов')
    # startwith, endwith - поле начинается*заканчивается
    
    # in - вхождение в набор значений 
    # posts = Post.objects.filter(title__in=('Заг1', 'Заг2'))

    # range - вхождение в диапозон/интервал
    # posts = Post.objects.filter(id__range=(1, 5))

    # gt, gte, lt, lte - сравнение значения поля >, >=, <, <=
    # posts = Post.objects.filter(id__gte=4)

    # year, month, day, week, week_day, time, hour, minute, second
    # Проверка поля по совпападению по отдельному из значений
    # posts = Post.objects.filter(pub_date__hour=17)

    # Комбинирование
    # posts = Post.objects.filter(pub_date__hour__gte=16)
    # posts = Post.objects.filter(pub_date__hour=16).filter(text__endwith='обновл')

    # По полям связанных объектов
    # posts = Post.objects.filter(author__username='Admin')
    # print( Post.objects.filter(author__username='Admin').query )

    # Сортировка объектов
    # posts = Post.objects.filter(author__username='Admin').order_by('-pub_date')
    # posts = Post.objects.filter(author__username='Admin').order_by('-pub_date')[:3] # Срез возвращает набор данных - первые 3
    
    # исключение отдельных полей
    # posts = Post.objects.defer('text).all()
    
    # count = Post.objects.count()

    # Агрегирующие функции
    # posts = Post.objects.aggregate( Max('id) )
    # posts = Post.objects.aggregate( Min('id) )
    # posts = Post.objects.aggregate( Sum('id) )
    # posts = Post.objects.aggregate( Count('id) )
    # posts = Post.objects.aggregate( Avg('id) )
                               
    # Получаем среднее число айдишников всех постов пользователям
    # annotate - расширение записей доп. полями как результат вычислений
    # users =  User.objects.annotate( posts_avg=Avg('posts__id') )
    # for elem in users:
    #    print(elem.posts_avg)


    context = {'current_id': 5, 'form': PostForm, 'posts': posts}
    return render(request, 'posts/posts_list.html', context)


def posts_detail(request, id):
    post = Post.objects.get_or_404(id = id)
    context = {'post': post}
    return render(request, 'posts/posts_detail.html', context)
