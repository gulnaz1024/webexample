from django.shortcuts import render, redirect
from django.template import context
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request,'webexample/index.html', {'title':'Main page of site', 'tasks':tasks})


def about(request):
    return render(request,'webexample/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была не верной '


    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request,'webexample/create.html',context)
