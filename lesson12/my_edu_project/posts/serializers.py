from rest_framework import serializers
from .models import Post, Category

class PostSerializer(serializers.ModelSerializer):
    # по умолчанию serializer.PrimaryKeyRelatedField
    # можем заменить на:
        # serializer.StringRelatedField,
        # serializer.SlugRelatedField,
        # serializer.HyperlinkedRelatedField
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ('title', 'text', 'pub_date', 'author', 'category')

class CategorySerializer(serializers.ModelSerializer):
    # Вместо id возвращаем стровоке представлеие объектов Post
    # posts = serializers.StringRelatedField(read_only=True, many=True)

    # Вместо id возвращаем сериализованные обхекты Post
    posts = PostSerializer(read_only=True, many=True)

    # добавляем новое поле, которого нет в модели
    count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('title', 'posts')

    # Вычисляем значение нового поля count
    def get_count(self, obj):
        return obj.posts.count()