from rest_framework import generics
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend

from .models import Post
from .serializers import PostSerializer

User = get_user_model()

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'author']

    # def get_queryset(self):
    #     # user = self.request.user
    #     # user_id = self.kwargs.get('id')
    #     user_id = self.request.query_params.get('id')
    #     user = User.objects.get(pk=user_id)
    #     return Post.objects.filter(author=user)