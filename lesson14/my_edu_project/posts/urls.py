from django.urls import path
from . import views


urlpatterns = [
    # path('', views.index, name='index'),

    # path('posts/', views.post_list, name='posts_list'),
    # path('posts/<int:pk>/', views.post_detail, name='posts_detail'),

    # path('posts/', views.APIPostList.as_view(), name='posts_list'),
    # path('posts/<int:pk>/', views.APIPostDetail.as_view(), name='posts_detail'),

    # path('posts/', views.PostList.as_view(), name='posts_list'),
    # path('posts/<int:pk>/', views.PostDetail.as_view(), name='posts_detail'),

    path('posts/', views.PostList2.as_view(), name='posts_list'),
    path('posts/<int:pk>/', views.PostDetail2.as_view(), name='posts_detail'),
]
