from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Task
from .serializers import TaskSerailzer
# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    # apis = ['/task-list/', '/task-detail/<str:pk>',
    #         '/task-update/<str:pk>', '/task-delete/<str:pk>/']

    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>',
        'Delete': '/task-delete/<str:pk>/',
    }
    return Response(api_urls)


@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskSerailzer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerailzer(tasks)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerailzer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request, pk):
    tasks = Task.objects.get(id=pk)

    serializer = TaskSerailzer(instance=tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
    tasks = Task.objects.get(id=pk)
    tasks.delete()
    return Response('Task sucessfully deleted !')
