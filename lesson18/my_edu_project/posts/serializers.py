from rest_framework import serializers
from .models import Post

BAD_WORD = ['блин', 'черт']


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор модели Post"""

    # post_author = serializers.StringRelatedField(source='author', readOnly=True)

    def to_representation(self, instance):
        return super().to_representation(instance)
    
    def to_internal_value(self, data):
        return super().to_internal_value(data)
    
    def validate(self, attr):
        return super().validate(attr)
    
    def validate_text(self, value: str) -> str:
        for word in BAD_WORD:
            if word in value.lower():
                raise serializers.ValidationError(f'Запрещено использовать {word}.')
        return value

    
    class Meta:
        model = Post
        fields = ('title', 'text', 'pub_date', 'author')


class PostListSerializer(serializers.ModelSerializer):
    """Сериализатор для списков Post"""

    class Meta:
        model = Post
        fields = ('title', 'author')


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категорий"""

    posts = PostListSerializer(read_only=True, many=True)
    count = serializers.SerializerMethodField()

    def get_count(self, obj) -> int:
        return self.posts.count()

    class Meta:
        model = Post
        fields = ['title']