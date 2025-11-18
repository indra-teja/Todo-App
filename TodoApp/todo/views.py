from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Task

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'home.html', {'tasks': tasks})

from datetime import datetime

@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        due_at_str = request.POST.get('due_at')

        if due_at_str:
            due_at = datetime.fromisoformat(due_at_str)
        else:
            due_at = None

        Task.objects.create(
            title=title,
            user=request.user,
            due_at=due_at
        )
    return redirect('home')

@login_required
def delete_task(request, id):
    task = Task.objects.get(id=id, user=request.user)
    task.delete()
    return redirect('home')

@login_required
def update_task(request, id):
    task = Task.objects.get(id=id, user=request.user)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.save()
        return redirect('home')
    return render(request, 'update.html', {'task': task})

@login_required
def mark_complete(request, id):
    task = Task.objects.get(id=id, user=request.user)
    task.completed = True
    task.save()
    return redirect('home')
