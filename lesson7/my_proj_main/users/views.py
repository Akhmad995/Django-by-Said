from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import MyForm

def register(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = MyForm()
        return render(request, 'registration/register.html', {'form': form})


# авторизация
def my_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('/')

    return render(request, 'registration/login.html')

# Выход
def my_logout(request):
    logout(request)
    return render(request, 'registration/logout.html')

