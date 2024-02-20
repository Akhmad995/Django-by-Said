from django.db import models
from django.contrib.auth import get_user_model
from .validators import validate_long_value


User = get_user_model()


class Post(models.Model):
    '''Модель публикации.'''
    title = models.CharField(max_length=255)
    text = models.TextField(validators=[validate_long_value])
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts'
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    is_visible = models.BooleanField(default=True)

    image = models.ImageField(
        'Изображение',
        blank=True,
        upload_to='posts/'
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title[:20]
