from django.utils import timezone
from rest_framework import serializers
from .models import Post



class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = (
            'title', 'text', 'author'
        )



class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title', 'author'
        )

