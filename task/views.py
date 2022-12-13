from django.shortcuts import render, redirect
from . models import Task
from .forms import TaskForm


def lists(request):
    tasks = Task.objects.order_by('-created_at')
    TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TaskForm()

    context = {
        'tasks': tasks,
        'form': form
    }
    return render(request, 'task/index.html', context)


def delete_complete(request):
    Task.objects.filter(completed__exact=True).delete()
    return redirect("/")


def delete_all(request):
    Task.objects.all().delete()
    return redirect("/")


def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('/')


def edit_task(request, pk):
    task = Task.objects.get(id=pk)
    edit = TaskForm(instance=task)
    if request.method == "POST":
        edit = TaskForm(request.POST, instance=task)
        if edit.is_valid():
            edit.save()
            return redirect("/")

    context = {
            "form": edit
        }
    return render(request, 'task/index.html', context)
