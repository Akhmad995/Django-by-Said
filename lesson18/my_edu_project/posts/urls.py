from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(r'posts', views.PostViewSet, basename='posts')

urlpatterns = [
    path( '', include(router.urls) ),
    path( 'categories/', views.CatetegoryList.as_view(), name='categories-list' ),
    path( 'categories/<int:pk>', views.CatetegoryDetail.as_view(), name='categories-detail' ),
]