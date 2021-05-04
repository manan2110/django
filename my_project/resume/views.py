from django.shortcuts import render
from .models import Resume
from django.core.mail import send_mail
from .forms import ContactMe

# Create your views here.

def home(request):
    return render(request , 'resume/home.html')

def about(request):
    resume = Resume.objects.get(pk = 1)
    return render(request , 'resume/about.html' , {"resume" : resume})

def contact(request):


    # form = ContactMe()
    # if request == "POST":
    #     form = ContactMe(request.POST)
    #     if form.is_valid():
    #         name = form.cleaned_data['name']
    #         subject = form.cleaned_data['subject']
    #         message = form.cleaned_data['message']
    #         email = form.cleaned_data['email']
    #         send_mail(subject , message , email , ['gyanchandanimanan@gmail.com'])
            

    if request.method == "POST":
        name = request.POST['name']
        subject = request.POST['subject']
        message = request.POST['message']
        email = request.POST['email']
        send_mail(subject , message , email , ['gyanchandanimanan@gmail.com'])
    return render(request , 'resume/contact.html')


def portfolio(request):
    return render(request , 'resume/portfolio.html')
