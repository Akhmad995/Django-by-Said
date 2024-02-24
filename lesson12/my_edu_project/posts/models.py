from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=150)


class Post(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
            User, 
            on_delete=models.SET_NULL,
            related_name='posts',
            null=True
        )
    category = models.ForeignKey(
            Category,
            on_delete=models.SET_NULL,
            related_name='posts',
            null=True
        )
