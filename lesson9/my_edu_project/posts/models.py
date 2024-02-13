from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='posts'
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title[:20]
