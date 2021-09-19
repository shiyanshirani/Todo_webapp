from django.shortcuts import render
from rest_framework.decorators import api_view
from .forms import TaskForm


def home(request):
    return render(request, "app/home.html")
