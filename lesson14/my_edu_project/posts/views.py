
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.decorators import action

from .models import Post
from .serializers import PostSerializer


# https://cdrf.co

# class PostViewSet(ReadOnlyModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=False, methods=['GET'])
    def last_updated(self, request):
        post = Post.objects.last()
        serializer = PostSerializer(post)
        return Response(serializer.data)
    