from rest_framework import serializers
from .models import Post



class PostSerializer(serializers.ModelSerializer):
    # Скрываем поле и указываем значение по умолчанию
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ('title', 'text', 'pub_date', 'author')


