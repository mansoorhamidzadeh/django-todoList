from django.shortcuts import render
from .models import Task
def index(request):
    note =Task.objects.all()

    return render(request,'base/index.html',context={'objects':note})