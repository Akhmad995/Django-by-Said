from django.urls import path
from .views import PostListAPIView

urlpatterns = [
    # path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    # path('', PostList.as_view(), name='post_list'),
    path('', PostListAPIView.as_view(), name='post_list')
]