from django.urls import path, include
from . import views


urlpatterns = [
    path( 'posts/', views.PostList.as_view(), name='post-list' )
]