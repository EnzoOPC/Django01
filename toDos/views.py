from django.shortcuts import render
from .models import Todo
from django.views.generic import ListView


def todo_list(request):
    todos = Todo.objects.all()
    return render(request, "toDos/todo_list.html", {"todos": todos})