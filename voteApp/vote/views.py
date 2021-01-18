from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout , login
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView, DetailView , CreateView , UpdateView , DeleteView

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Candidates


# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        #check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
        # A backend authenticated the credentials
            return redirect("/")
        else:
            return render(request,'login.html')
        # No backend authenticated the credentials
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")


def Vote(request, pk):
    post = get_object_or_404(Candidates, id=request.POST.get('id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('blogpost-detail', args=[str(pk)]))


class VoteDetails(DetailView):
    model = Candidates
    # template_name = MainApp/BlogPost_detail.html
    # context_object_name = 'object'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        votes_connected = get_object_or_404(Candidates, id=self.kwargs['pk'])
        voted = False
        if votes_connected.likes.filter(id=self.request.user.id).exists():
            voted = True
        data['number_of_votes'] = votes_connected.number_of_likes()
        data['candidate_is_voted'] = voted
        return data