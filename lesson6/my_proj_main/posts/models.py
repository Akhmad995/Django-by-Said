# Модели
from django.db import models
from django.contrib.auth import get_user_model


RATING = [(1, 'Плохо'), (2, 'Посредственно'), (3, 'Нормально'), (4, 'Хорошо')]


# Модель пользователя встроена в Django и импортируется следующим образом:
User = get_user_model()


# Модель публикаций
class Post(models.Model):
    title = models.CharField(
        max_length=100        
    )
    text = models.TextField(null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
    )

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return f'{self.title[:30]} -- {self.pub_date}'
