from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.ModelSerializer):
    """Сериализатор модели News"""
    
    # Скрываем поле и указываем значение по умолчанию
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = News
        fields = ('title', 'text', 'pub_date', 'author')


