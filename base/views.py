# third party imports
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

# local imports
from .models import *
from .forms import TaskFrom


# =============== homepage view =============== 
def homepage(request):
    q = request.GET.get('search', '').strip()  

    active_tasks = Todo.objects.filter(is_completed=False)
    if q:  
        active_tasks = active_tasks.filter(title__icontains=q)
    active_tasks = active_tasks.order_by("deadline")

    completed_tasks = Todo.objects.filter(is_completed=True)
    if q:
        completed_tasks = completed_tasks.filter(title__icontains=q)
    completed_tasks = completed_tasks.order_by("-deadline")

    # PAGINATORS
    active_paginator = Paginator(active_tasks, 4)
    active_page_number = request.GET.get("page_active")
    active_page_obj = active_paginator.get_page(active_page_number)

    completed_paginator = Paginator(completed_tasks, 4)
    completed_page_number = request.GET.get("page_completed")
    completed_page_obj = completed_paginator.get_page(completed_page_number)

    context = {
        "active_tasks": active_page_obj,
        "completed_tasks": completed_page_obj,
        "q": q
    }

    return render(request, 'base/homepage.html', context)



# =============== toggle tasks view =============== 
def toggle_complete(request, pk):
    todo = get_object_or_404(Todo, id=pk)

    todo.is_completed = not todo.is_completed
    todo.save()

    return redirect("homepage")



# =============== create task view =============== 
def create_task(request):
    page = "create-task"

    form = TaskFrom()

    if request.method == "POST":
        form = TaskFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    context = {
        "form" : form,
        "page" : page
    }
    return render(request, 'base/task_form.html', context)



# =============== update task view =============== 
def update_task(request, pk) :
    todo = get_object_or_404(Todo, id=pk)

    form = TaskFrom(instance=todo)
    if request.method == "POST":
        form = TaskFrom(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("homepage")
        
    context = {
        "form" : form
    }
    return render(request, 'base/task_form.html', context)



# =============== delete task view =============== 
def delete_task(request, pk):

    todo = get_object_or_404(Todo, id=pk)

    if request.method == "POST":
        todo.delete()
        return redirect("homepage")

    context = {
        "todo" : todo
    }
    return render(request, 'base/delete_task.html', context)