from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login

# Create your views here.


def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'home.html')


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')
        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        if user is not None and user.role == role:
            login(request, user)
        # A backend authenticated the credentials
            return redirect("/")
        else:
            return render(request, 'login.html')
        # No backend authenticated the credentials
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect("/login")
