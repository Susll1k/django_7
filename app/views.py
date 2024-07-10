from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Todo

def list_todo(request):
    tasks = Todo.objects.all()
    if request.method == 'POST':
        tasks = Todo.objects.filter(title = request.POST['title'])
        if request.POST['title'] == '':
            tasks = Todo.objects.all()
    return render(request, 'home.html', {'tasks': tasks})
