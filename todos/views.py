from django.http import HttpResponse
from django.shortcuts import render
from .models import Todo

def todo_list(request):
    todos = Todo.objects.all()
    context = {
        "todo_list": todos
    }
    return render(request, "todos/todo_list.html", context=context)
