from django.utils import timezone
from rest_framework import serializers
from .models import Post



class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault()) # Скрываем поле и указываем значение по умолчанию

    class Meta:
        model = Post
        fields = (
            'title', 'text', 'author'
        )


