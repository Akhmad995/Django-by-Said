from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Post

User = get_user_model()

admin.site.register(Post)
admin.site.register(User)
