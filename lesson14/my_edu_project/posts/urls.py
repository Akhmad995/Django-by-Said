from django.urls import path, include
from rest_framework.routers import  DefaultRouter, SimpleRouter
from . import views

router = DefaultRouter()
# router = SimpleRouter()

router.register( r'posts', views.PostViewSet )

urlpatterns = [
    path( '', include( router.urls ) )
]