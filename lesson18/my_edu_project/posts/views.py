from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics

from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer, PostListSerializer
from .permissions import iAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def get_queryset(self):
    #     return super().get_queryset()

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        return PostListSerializer

    def get_permissions(self):
        return super().get_permissions()

    @action(detail=False, methods=['get'])
    def my_post(self, request) -> Response:
        posts = Post.objects.filter(author=request.user)
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)


class CatetegoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CatetegoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
