from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.models import Task
from .serializers import TaskSerializer


@api_view(['GET'])
def todoListApiView(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, context={'request': request}, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def todoListDetailApiView(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, context={'request': request}, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def todoListCreateApiView(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT'])
def todoListUpdateApiView(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def todoListDeleteApiView(request,pk):
    task=Task.objects.get(id=pk)
    task.delete()
    return Response(status=204)