from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import Task


def index(request):
    tasks = Task.objects.filter(author__exact=None)
    return render(request, 'main/index.html', {'title': 'Main page', 'tasks': tasks})


def user(request):
    tasks = Task.objects.filter(author__exact=request.user.username, is_done__exact=False)
    return render(request, 'main/user_profile.html', {'tasks': tasks})


@login_required
def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.author = request.user.username
            new_task.save()
            return redirect('user_page')
        else:
            error = 'Form is not valid'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
