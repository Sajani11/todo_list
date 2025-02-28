# todos/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm # type: ignore

# View to list all Todo items
def todo_list(request):
    todos = Todo.objects.all()  # Fetch all Todo items from the database
    return render(request, 'todos/todo_list.html', {'todos': todos})

# View to add a new Todo item
def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new Todo item to the database
            return redirect('todo_list')  # Redirect to the Todo list page
    else:
        form = TodoForm()
    return render(request, 'todos/add_todo.html', {'form': form})

# View to update an existing Todo item
def update_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()  # Save the updated Todo item to the database
            return redirect('todo_list')  # Redirect to the Todo list page
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todos/update_todo.html', {'form': form, 'todo': todo})

# View to delete a Todo item
def delete_todo(request, pk):
    todo = get_object_or_404(todo, pk=pk)
    if request.method == 'POST':
        todo.delete()  # Delete the Todo item from the database
        return redirect('todo_list')  # Redirect to the Todo list page
    return render(request, 'todos/confirm_delete.html', {'todo': todo})
