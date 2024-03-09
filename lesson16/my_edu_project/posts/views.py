from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
# from rest_framework.permissions import IsAuthenticated

from .models import Post
from .serializers import PostSerializer
from .pagination import PostPagination
from .permissions import isAdminOrReadOnly, iAuthorOrReadOnly


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    # permission_classes = (IsAutenticated,)
    permission_classes = (isAdminOrReadOnly,)
    # отключение пашинайии для отдельного вьюсета
    # pagination_class = None

    def get_permissions(self):
        if self.action == 'create':
            return (iAuthorOrReadOnly(),)
        return super().get_permissions()
    