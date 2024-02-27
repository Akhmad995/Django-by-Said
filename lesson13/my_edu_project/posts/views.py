from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Post
from .serializers import PostSerializer


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


def post_detail(request, pk):
    pass