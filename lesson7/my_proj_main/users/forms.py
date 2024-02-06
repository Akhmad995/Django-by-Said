from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class MyForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'birth_date', 'is_married']
        