from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination

from .models import Post
from .serializers import PostSerializer
from .pagination import PostPagination


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    # отключение пашинайии для отдельного вьюсета
    # pagination_class = None
    