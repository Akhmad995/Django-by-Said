from django.urls import path, include
from rest_framework.routers import  DefaultRouter, SimpleRouter
from . import views

router = DefaultRouter()
# router = SimpleRouter()

router.register( r'posts', views.PostViewSet, basename='my_posts' )
router.register( r'posts1', views.PostViewSet, basename='my_posts1' )

urlpatterns = [
    path( '', include( router.urls ) )
]