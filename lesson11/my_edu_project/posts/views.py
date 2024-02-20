from rest_framework import generics
from rest_framework import filters
from rest_framework import permissions

from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()

    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_field = ['title']


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()

    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated)

