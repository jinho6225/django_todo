from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

def todo_list(request):
    todos = Todo.objects.all()
    context = {
        "todo_list": todos
    }
    return render(request, "todos/todo_list.html", context)

#CRUD - Create, Retrieve, Update, Delete, List

def todo_detail(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        "todo": todo
    }
    return render(request, "todos/todo_detail.html", context)

def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        # print(form.cleaned_data)
        # name = form.cleaned_data['name']
        # due_date = form.cleaned_data['due_date']
        # new_todo = Todo.objects.create(name=name, due_date=due_date)
        form.save()
        return redirect('/')

    context = {"form": form}
    return render(request, "todos/todo_create.html", context)