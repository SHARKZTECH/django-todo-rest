from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TaskSerializer
from .models import Task


@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'List': '/task-list/',
        'Detail': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/tast-update/<str:pk>/',
        'Delete': '/tast-delete/<str:pk>/'
    }
    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    tasts = Task.objects.all()
    serializer = TaskSerializer(tasts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Item deleted succefully")
