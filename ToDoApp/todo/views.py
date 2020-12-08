from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem

# Create your views here.
def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request,'todo.html',{'all_items':all_todo_items})

def addTodo(request):
    a = request.POST['content']
    new_item = TodoItem(content = a)
    new_item.save()
    return HttpResponseRedirect('/todo/')

def deleteTodo(request,todo_id):
    item = TodoItem.objects.get(id=todo_id)
    item.delete()
    return HttpResponseRedirect('/todo/')