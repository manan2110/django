from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerialzer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.test import force_authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.authentication import JWTAuthentication
import requests
from requests.auth import HTTPBasicAuth
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.


def get_api_route(request):
    domain = get_current_site(request=request).domain
    return "http://" + domain + "/auth"


@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all().order_by('-id')
    user = request.user
    force_authenticate(request, user=user)
    serializer = TaskSerialzer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test(request):
    return Response(data='hi', status=status.HTTP_200_OK)


@api_view(['GET'])
def new(request):
    # username = 'trying'
    # password = 'trying@123'
    mytoken = ''
    # user = authenticate(username=username, password=password)
    user = request.user
    if user is not None:
        mytoken = Token.objects.get(user=user).key
    d = requests.get('http://127.0.0.1:8000/auth/hi',
                     headers={'Authorization': 'Token {}'.format(mytoken)})
    return Response(data=d.json(), status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def test2(request):
    return Response(data='hi', status=status.HTTP_200_OK)


@api_view(['GET'])
def new2(request):
    username = 'trying'
    password = 'trying@123'
    mytoken = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIzODU0ODU5LCJqdGkiOiI0ZWQ4ZTgwMGQ3OWI0YjQxYTQzZWIzOWE5YjA1ZjhhOCIsInVzZXJfaWQiOjF9.r5mqscDuOco8fHQU6tPlVpkwgkA7MpndHGQ-4cPVp0Y'
    d = requests.get('http://127.0.0.1:8000/auth/hi2',
                     headers={'Authorization': 'Bearer {}'.format(mytoken)})
    return Response(data=d.json(), status=status.HTTP_200_OK)
