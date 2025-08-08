from django.shortcuts import HttpResponse, redirect
from django.shortcuts import render
from .models import Task

# Create your views here.
def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')