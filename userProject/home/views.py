from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.views.decorators.csrf import csrf_protect
from .models import Config
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
from sawo import createTemplate, getContext, verifyToken
import json
import os


# def loginUser(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         # check if user has entered correct credentials
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             # A backend authenticated the credentials
#             return redirect("/")
#         else:
#             return render(request, "login.html")
#         # No backend authenticated the credentials
#     return render(request, "login.html")


# def logoutUser(request):
#     logout(request)
#     return redirect("/login")


# @csrf_exempt
# def index(request):
#     context = {
#         "sawo": {
#             "auth_key": "81caf9e7-416a-4961-972f-9971725c1e15",
#             "identifier": "email",
#             "to": "login",
#         }
#     }
#     return render(request, "partials/_sawo.html", context)


# @csrf_exempt
# def login(request):
#     username = "mg"
#     password = "test@123"
#     # check if user has entered correct credentials
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         login(user)
#     payload = request.POST.get("data")
#     if verifyToken(payload):
#         print("hello")
#         return redirect("/")
#         # do something
#     else:
#         print("not hello")
#         return redirect("/login")
#         # do something else
#     logout(request)


load = ""
loaded = 0


def setPayload(payload):
    global load
    load = payload


def setLoaded(reset=False):
    global loaded
    if reset:
        loaded = 0
    else:
        loaded += 1


def index(request):
    return render(request, "index.html")


def login(request):
    setLoaded()
    setPayload(load if loaded < 2 else "")
    config = {
        "auth_key": "81caf9e7-416a-4961-972f-9971725c1e15",
        "identifier": "email",
        "to": "receive",
    }
    context = {"sawo": config, "load": load, "title": "Home"}
    return render(request, "login.html", context)


@csrf_exempt
def receive(request):
    if request.method == "POST":
        print(request.body)
        payload = json.loads(request.body)["payload"]
        print(payload)
        setLoaded(True)
        setPayload(payload)
        print(payload)
        if verifyToken(payload):
            print("hello")
        status = 200
        print(status)
        response_data = {"status": status}
        return HttpResponse(json.dumps(response_data), content_type="application/json")
