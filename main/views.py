from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import Task


def index(request):
    tasks = Task.objects.filter(author__exact=None)
    return render(request, 'main/index.html', {'title': 'Main page', 'tasks': tasks})


@login_required(redirect_field_name='main/index.html')
def user(request):
    tasks = Task.objects.filter(author__exact=request.user.username, is_done__exact=False)
    done_tasks = Task.objects.filter(author__exact=request.user.username, is_done__exact=True)
    return render(request, 'main/user_profile.html', {'title': request.user.username,
                                                      'tasks': tasks,
                                                      'done_tasks': done_tasks})


def change_state_by_id(request, task_id):
    task = Task.objects.get(pk=task_id)
    try:
        task.is_done = not task.is_done
        task.save()
        return redirect('/user')
    except Exception:
        pass


def ajax_change_status(request):
    print("inside")
    task_id = request.GET.get('id', False)
    task = Task.objects.get(pk=task_id)
    try:
        task.is_done = not task.is_done
        task.save()
        return JsonResponse({"success": True})
    except Exception as e:
        return JsonResponse({"success": False})
    # return JsonResponse(data)


@login_required
def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.author = request.user.username
            new_task.is_done = False
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
