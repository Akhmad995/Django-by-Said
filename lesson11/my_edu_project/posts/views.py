# from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer


# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    


# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class PostListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)

        print( 'serializer', serializer, type(serializer), sep='   |   ' )
        print('****')
        print( 'serializer.initial_data', serializer.initial_data, type(serializer.initial_data), sep='   |   ' )
        print('****')

        if serializer.is_valid():
            print( 'serializer', serializer, type(serializer), sep='   |   ' )
            print('****')
            print( 'serializer.initial_data', serializer.initial_data, type(serializer.initial_data), sep='   |   ' )
            print('****')

            serializer.save()

            print( 'serializer', serializer, type(serializer), sep='   |   ' )
            print('****')
            print( 'serializer.data', serializer.data, type(serializer.data), sep='   |   ' )
            print('****')
            print( 'serializer.initial_data', serializer.initial_data, type(serializer.initial_data), sep='   |   ' )
            print('****')
            
            return Response(serializer.data, status=201)
        return Response(serializer.error, status=400)
