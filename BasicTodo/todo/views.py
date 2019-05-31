from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone

from .models import TodoList

def index(request):
    user = auth.get_user(request)
    if not user.is_authenticated:
        return render(request, 'todo/index_not_login.html')
    
    latest_todolist = user.todolist_set.order_by('-last_mod')
    context = {
        'latest_todolist' : latest_todolist
    }
    return render(request, 'todo/index_login.html', context)


def create(request):
    if request.method == 'POST':
        user = auth.get_user(request)
        user.todolist_set.create(
            todo_content=request.POST['new_todo'],
            pub_date=timezone.now(),
            last_mod=timezone.now()
        )
        return redirect('base')

    return redirect('base')


def update(request, pk):
    if request.method == "POST":
        todolist = get_object_or_404(TodoList, pk=pk)
        todolist.modify_content(request.POST['modified_content'])
        todolist.save()
        return redirect('base')

    return redirect('base')

def change_todo_complete(request, pk):
    if request.method == "POST":
        todolist = get_object_or_404(TodoList, pk=pk)
        todolist.change_complete()
        todolist.save()
        return redirect('base')

    return redirect('base')


def delete(request, pk):
    if request.method == "POST":
        todolist = get_object_or_404(TodoList, pk=pk)
        todolist.delete()
        return redirect('base')

    return redirect('base')