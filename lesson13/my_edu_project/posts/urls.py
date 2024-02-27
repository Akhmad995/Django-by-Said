from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.post_list, name='posts_list'),
    path('posts/<int:pk>/', views.post_detail, name='posts_detail'),
]
