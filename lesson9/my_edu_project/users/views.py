from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import MyUserForm


class RegisterView(CreateView):
    form_class = MyUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')