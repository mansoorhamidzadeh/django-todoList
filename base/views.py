from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForms


def todoList(request):
    tasks = Task.objects.all()
    context = {
        'objects': tasks
    }
    return render(request, 'base/index.html', context)


def todoListDetail(request, pk):
    task = Task.objects.get(id=pk)
    context = {
        'object': task
    }
    return render(request, 'base/detail.html', context)


@login_required
def todoListCreate(request):
    form = TaskForms()
    if request.method == 'POST':
        form = TaskForms(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('todoList')

    context = {
        'form': form
    }
    return render(request, 'base/create.html', context)


@login_required
def todoListUpdate(request, pk):
    task = Task.objects.get(id=pk)
    print(task)
    form = TaskForms(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('todoList')
    context = {

        'form': form
    }
    return render(request, 'base/create.html', context)


@login_required
def todoListDelete(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('todoList')
    return render(request, 'base/delete.html')
