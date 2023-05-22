from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, newTask
from .forms import TaskForm


# Create your views here.

def delete(request, id):
    task =get_object_or_404(newTask, id=id)
    context = {'task': task}
    task.delete()
    return redirect('home')
    
def index(request):
    tasks = Task.objects.order_by('-id')
    newtasks = newTask.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks, 'newtasks': newtasks,})

def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = TaskForm()
    context = {
        'form' : form,
        'error': error
    }
    return render(request, 'main/create.html', context)


        

