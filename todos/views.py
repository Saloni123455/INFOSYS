from django.shortcuts import render
from django.template.defaultfilters import title

from .models import Todo

# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request,template_name='todos/todo_list.html',context=context)
def add_todo(request):
    if request.method == "POST":
        title = request.POST['title']
        if title:
            Todo.objects.create(title=title)
    return render(request,template_name='todos/add_todo.html')