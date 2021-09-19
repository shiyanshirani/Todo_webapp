from django.shortcuts import render
from rest_framework.decorators import api_view
from .forms import TaskForm



def home(request):
    context = {}
    
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = TaskForm()
    return render(request, 'app/home.html', context)