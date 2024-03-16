from rest_framework import generics
from django.contrib.auth import get_user_model

from rest_framework.filters import OrderingFilter

from .models import Post
from .serializers import PostSerializer

User = get_user_model()


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    filter_backends = [OrderingFilter]
    ordering_fields = ['title', 'text']
    ordering = ['-text']
