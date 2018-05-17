from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Todo
from .forms import TodoForm
from django.views.decorators.http import require_POST

def index(request):
    todo_list = Todo.objects.order_by('due_date')
    form = TodoForm
    context = {'todo_list' : todo_list, 'form':form}
    return render(request,'index.html',context)

class addTodo(CreateView):
    model = Todo
    fields = ['text','due_date']

def completeTodo(request,todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')

def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('index')

def deleteAll(request):
        Todo.objects.all().delete()
        return redirect('index')
