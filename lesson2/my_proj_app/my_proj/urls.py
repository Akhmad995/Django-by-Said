from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('posts.urls', namespace='posts')),
    path('admin/', admin.site.urls),
]

# <a href="{% url 'posts:posts_list' %}">Ссылка</a>


