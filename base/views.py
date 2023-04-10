from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

from .models import Task
from .forms import TaskForms, LoginForm, RegisterForm


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



def LoginView(request):
    if request.method=='POST':
        form =LoginForm(request.POST)

        if form.is_valid():
            username=request.POST.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username
                              ,password=password)
            if user is not None:
                login(request,user)
                return redirect('todoList')
    else:
        form=LoginForm()

    context={
        'form':form
    }
    return render(request,'base/login.html',context)

def registerView(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todoList')
    else:
        form=RegisterForm()


    return render(request,'base/login.html',{'form':form})

# class LoginView(LoginView):
#     template_name='base/login.html'
#     fields='__all__'
#     redirect_authenticated_user=True
#     def get_success_url(self):
#         return reverse_lazy('todoList')