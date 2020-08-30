from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import ToDo
from .forms import ToDoForm


def todo_list_view(request):
    queryset = ToDo.objects.filter(completed=False)
    context ={
    'object_list': queryset,
    }
    template_name = 'fbv_todo/todo_list.html'
    return render(request, template_name, context)

def todo_completed_list_view(request):
    queryset = ToDo.objects.filter(completed=True)
    context ={
    'object_list': queryset,
    'complete': True,
    }
    template_name = 'fbv_todo/todo_list.html'
    return render(request, template_name, context)

def todo_detail_view(request, id):
    queryset = get_object_or_404(ToDo, id=id) 
    context ={
    'object': queryset,
    }
    template_name = 'fbv_todo/todo_detail.html'
    return render(request, template_name, context)

def todo_create_view(request):
    form = ToDoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Item added successfully, Add another')
        return redirect('todo:todo_create') 
    context ={
    'form': form,
    }
    template_name = 'fbv_todo/todo_create.html'
    return render(request, template_name, context)

def todo_update_view(request, id):
    queryset = get_object_or_404(ToDo, id=id) 
    if request.method == 'POST' and queryset.completed == True:
        queryset.completed = False
        queryset.save()
    form = ToDoForm(request.POST or None, instance=queryset)
    if form.is_valid():
        form.save()
        return redirect('todo:todo_list') 
    context ={
    'object': queryset,
    'form': form,
    }
    template_name = 'fbv_todo/todo_update.html'
    return render(request, template_name, context)


def todo_delete_view(request, id):
    queryset = get_object_or_404(ToDo, id=id)
    if request.method == 'POST':
        queryset.delete()
        return redirect('todo:todo_list') 
    context ={
    'object': queryset,
    }
    template_name = 'fbv_todo/todo_delete.html'
    return render(request, template_name, context)

def todo_mark_as_completed_or_incompleted_view(request, id):
    queryset = get_object_or_404(ToDo, id=id)
    if queryset.completed == False:
        queryset.completed = True
    else:
        queryset.completed = False
    queryset.save()    
    return redirect('todo:todo_list')



