from django.http import request, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.

def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/') # redirects the site to the main html site

    context = {'tasks':tasks, 'form':form}
    return render(request, 'tasks/list.html', context)


def updateTask(request, pk): # pk is primary key
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')


    context = {'form':form}

    return render(request, 'tasks/update_task.html', context)


def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return HttpResponseRedirect('/')

    context = {'item':item}

    return render(request, 'tasks/delete.html', context)