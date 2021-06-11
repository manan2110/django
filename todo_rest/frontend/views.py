from django.shortcuts import render

# Create your views here.


def list(request):
    print(request.user.is_authenticated)
    return render(request, 'list.html')
