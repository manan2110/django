from django.shortcuts import render
from .models import Resume
from .forms import ContactMe

# Create your views here.

def home(request):
    return render(request , 'resume/home.html')

def about(request):
    resume = Resume.objects.get(pk = 1)
    return render(request , 'resume/about.html' , {"resume" : resume})

def contact(request):
    form = ContactMe()
    return render(request, 'resume/contact.html' , {'form' : form})