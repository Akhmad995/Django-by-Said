from django.db import models
#from django.contrib.auth.models import AbstractUser, AbstractBaseUser 
from django.contrib.auth.models import AbstractUser

# Создаем кастомный класс пользователей до первых миграций

class CustomUser(AbstractUser):
    birth_date = models.DateField(null=True)
    is_married = models.BooleanField(null=True)
