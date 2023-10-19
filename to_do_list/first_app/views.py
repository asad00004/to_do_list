from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import TaskModel

# Create your views here.

def add_task(request):
    if request.method == "POST":
        task = TaskForm(request.POST)
        if task.is_valid():
            task.save()
            return redirect("add")
    return render(request, 'add_task.html', {'form': TaskForm})

def show_tasks(request):
    task = TaskModel.objects.all()
    return render(request, 'show_tasks.html', {'data': task})

def edit_task(request, id):
    task = TaskModel.objects.get(pk= id)
    form = TaskForm(instance= task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance= task)
        if form.is_valid():
            form.save()
            return redirect("show")
    return render(request, 'add_task.html', {'form': form})

def delete_task(request, id):
    TaskModel.objects.get(pk= id).delete()
    return redirect("show")

def completed_task_list(request):
    task = TaskModel.objects.all()
    return render(request, 'completed_tasks.html', {'data': task})

def complete_task(request, id):
    task = TaskModel.objects.get(pk= id)
    task.is_completed = True
    task.save()
    return redirect('completed_list')