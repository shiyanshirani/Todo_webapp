from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from .forms import * 
from .models import *

def home(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    context = {'tasks': tasks, 'form': form}
    
    return render(request, "app/home.html", context)

def update_task(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")
    
    context = {"form": form}
    
    return render(request, 'app/update_task.html', context)

def delete_task(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == "POST":
        task.delete()
        return redirect("/")
    context = {'task': task}
    
    return render(request, 'app/delete_task.html', context)
    