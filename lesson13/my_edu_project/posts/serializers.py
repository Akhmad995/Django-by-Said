from django.utils import timezone
from rest_framework import serializers
from .models import Post


class BigName(serializers.Field):
    def to_representation(self, value):
        return value.upper()

    def to_internal_value(self, data):
        data = data[0] + data[1:].lower()
        return data


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    title = BigName()

    
    def validate(self, attrs):
        if attrs['title'] not in attrs['text']:
            raise serializers.ValidationError(
                'Заголовок статьи должен фигурировать в тексте.')
        return attrs


    def validate_pub_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError(
                'Публикация статьи не может произойти в прошлом.')
        return value

    class Meta:
        model = Post
        fields = (
            'title', 'text', 'pub_date', 'create_date', 'author'
        )


