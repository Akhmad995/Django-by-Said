
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, ViewSet, GenericViewSet
from rest_framework.decorators import action
from rest_framework import mixins

from .models import Post
from .serializers import PostSerializer, PostListSerializer


# https://cdrf.co

# class PostViewSet(ReadOnlyModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


    def create(self, request, *args, **kwargs):
        return super().create(request, *args, partical=True, **kwargs)


    @action(detail=False, methods=['GET'])
    def last_updated(self, request):
        post = Post.objects.last()
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        return PostSerializer
    
    def get_queryset(self):
        new_set = Post.objects.filter(pub_date__month__gte=3)
        return new_set
    

class BasePostViewset(ViewSet):
    def list(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        pass

    def retrieve(self, request):
        pass

    def update(self, request):
        pass

    def partial_update(self, request):
        pass

    def destroy(self, request):
        pass


# Кастомный viewset создается через GenericViewSet
class ListCreateRetrieveUpdateViewset(ViewSet, 
                                      mixins.ListModelMixin,
                                      mixins.CreateModelMixin,
                                      mixins.RetrieveModelMixin,
                                      mixins.UpdateModelMixin,
                                      GenericViewSet):
    """
    Вьюсет с разрешеными методами list, create, retrieve, update
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


