from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Category(models.Model):
    title = models.CharField('Название категории', max_length=155, blank=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.title[:20]
    
class Tag(models.Model):
    name = models.SlugField('Имя тега', max_length=15, null=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Теги'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.title[:20]


class Post(models.Model):
    """Модель постов"""

    title = models.CharField('Заголовок поста', max_length=155, blank=False)
    text = models.TextField('Текст поста', blank=False)
    create_date = models.DateTimeField('Дата создания', auto_now_add=True)
    update_date = models.DateTimeField('Дата изменения', auto_now=True)
    pub_date = models.DateTimeField('Дата публикации', default=timezone.now)
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts',
        verbose_name='Автор поста'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts',
        verbose_name='Категория поста'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='posts',
        through='PostTag',
        verbose_name='Теги публикации'
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self) -> str:
        return self.title[:20]


class PostTag(models.Model):
    """Промежуточная таблица для тегов Многие ко Многим"""
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE
    )

    class Meta:
        constraints = [ models.UniqueConstraint( fields=['post', 'tag'], name='post-tag' ) ]