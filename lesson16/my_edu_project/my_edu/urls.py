from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('api/v1/', include( ('posts.urls', 'posts'), namespace='posts') ),
    # path('auth/', include( ('rest_framework.urls')) ),
    # re_path(r'auth/', include('djoser.urls')),
    # re_path(r'auth/', include('djoser.urls.authtoken')),

    path( 'token/', TokenObtainPairView.as_view(), namespace='token_obtain')
    path( 'token/refresh/', TokenRefreshView.as_view(), namespace='token_refresh')
]
