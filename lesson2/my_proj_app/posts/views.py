from django.shortcuts import render, HttpResponse
from .forms import PostForm

def index(request):
    context = {'username': 'Saeed'}
    return render(request, 'index.html', context)

def posts_list(request):
    return HttpResponse("Список публикации")

def posts_detail(request, pk):
    return HttpResponse('Детельная публикации', pk)

def form(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            date = form.cleaned_data['date']
            return HttpResponse(f'{title}, {text}, {date}')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'form.html', context)