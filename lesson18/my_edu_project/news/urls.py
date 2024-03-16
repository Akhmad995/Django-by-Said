from django.urls import path, include
from . import views


urlpatterns = [
    path( '', views.index, name='news' ),
    path( 'news/', views.NewsList.as_view(), name='news' ),
    path( 'news/<int:pk>', views.NewsDetail.as_view(), name='news-detail' )
]