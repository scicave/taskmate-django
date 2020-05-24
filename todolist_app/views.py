from django.shortcuts import render,redirect
from .models import TaskList
from django.shortcuts import get_object_or_404
from .forms import taskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@ login_required
def todolist(request):
    if request.method == 'POST':
        form=taskForm(request.POST or None)
        if form.is_valid():
           instance=form.save(commit=False)
           instance.user=request.user
           instance.save()
        messages.success(request,('success adding task'))
        return redirect('todolist')
    else:
        all_tasks = TaskList.objects.filter(user=request.user)
        p=Paginator(all_tasks,5)
        page = request.GET.get('page')
        all_tasks=p.get_page(page)
        return render(request,'todolist_app/todolist.html',{'all_tasks':all_tasks})

@login_required
def delete_task(request,task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.user==request.user:
       task.delete()
    else:
        messages.error(request,('Access restricted'))
    return redirect('todolist')
@login_required
def complete_task(request,task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.user==request.user:
      task.done=True
      task.save()
    else:
        messages.erroe(request,('Access restricted'))
    return redirect('todolist')
@login_required
def pending_task(request,task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done=False
    task.save()
    return redirect('todolist')

def edit(request,task_id):
   if request.method == 'POST':
        task=TaskList.objects.get(pk=task_id)
        form=taskForm(request.POST or None,instance=task)
        if form.is_valid():
            form.save()
        messages.success(request,('task edited'))
        return redirect('todolist')
   else:
        task_obj= get_object_or_404(TaskList,pk=task_id)
        return render(request,'todolist_app/edit.html',{'task_obj':task_obj})



def contact(request):
    return render(request,'todolist_app/contact.html')

def about(request):
    return render(request,'todolist_app/about.html')

def index(request):
    return render(request,'todolist_app/index.html')
