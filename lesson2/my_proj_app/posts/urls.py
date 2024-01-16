from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index),
    path('form/', views.form, name='posts_form'),
    path('posts/', views.posts_list, name='posts_list'),
    path('posts/<int:pk>', views.posts_detail, name='posts_detail'),
]

