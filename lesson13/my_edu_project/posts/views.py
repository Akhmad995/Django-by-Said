from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Post
from .serializers import PostSerializer


# ****** Первый способ *****

@api_view(['GET', 'POST'])
def index(request):
    """
    Главная страница
    """
    if request.method == 'POST':
        return Response({ 
            'message': 'Получены данные',
            'data': request.data 
        })
    
    return Response({
        'message': 'Главная страница'
    })


@api_view(['GET', 'POST'])
def post_list(request):
    """
    Получаем список публикаций или создаем новые
    """
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)    
        return Response(serializer.data,  status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def post_detail(request, pk):
    """
    Получаем, изменяем или удаляем отдельную публикацию.
    """

    post = get_object_or_404(Post, pk=pk)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    elif request.method == 'PUT' or request.method == 'PATCH':
        # аргумент partial позволяет передавать не все аргументы
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ****** Второй способ *****

class APIPostList(APIView):
    """
    Получаем список публикаций или создаем новые
    """
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)    
        return Response(serializer.data,  status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class APIPostDetail(APIView):
    """
    Получаем, изменяем или удаляем отдельную публикацию.
    """
    def get(self, request, pk=None, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk=None, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        # аргумент partial позволяет передавать не все аргументы
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# ****** Третий способ *****

class PostList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    """
    Получаем список публикаций или создаем новые
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request,  *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class PostDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    """
    Получаем, изменяем или удаляем отдельную публикацию.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, pk=None, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, pk=None, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, pk=None, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    


# ****** Четвертый способ *****
    
class PostList2(generics.ListCreateAPIView):
    """
    Получаем список публикаций или создаем новые
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail2(generics.RetrieveUpdateDestroyAPIView):
    """
    Получаем, изменяем или удаляем отдельную публикацию.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer