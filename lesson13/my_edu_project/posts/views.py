from rest_framework import generics
from .models import Post
from .serializers import PostSerializer


# Представление для списка ресурсов публикаций
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# Представление для отдельного ресурса публикаций
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


