from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.shortcuts import render


# Create your views here.
from TO_DO_list.forms import TaskForm
from TO_DO_list.models import STATUS, Task


def index_view(request):
    tasks = Task.objects.all()
    context = {"tasks": tasks}
    return render(request, "index.html", context)

def task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, "task.html", {"task": task})




def delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        return render(request, "delete.html", {"task": task})
    else:
        task.delete()
        return redirect("index_view")




def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        form = TaskForm(initial={
            "name_of_task": task.name_of_task,
            "description": task.description,
            "status": task.status,
            "task_data": task.task_data,
        })
        return render(request, "update.html", {"form": form})
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.name_of_task = form.cleaned_data.get("name_of_task")
            task.description = form.cleaned_data.get("description")
            task.status = form.cleaned_data.get("status")
            task.task_data = form.cleaned_data.get("task_data")
            task.save()
            return redirect("task_view", pk=task.pk)
        return render(request, "update.html", {"form": form})



def create_task(request):
    if request.method == "GET":
        form = TaskForm()
        # return render(request, "create.html", {"statuses": STATUS})
        return render(request, "create.html", {"form": form})
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            name_of_task = form.cleaned_data.get("name_of_task")
            description = form.cleaned_data.get("description")
            status =  form.cleaned_data.get("status")
            task_data = form.cleaned_data.get("task_data")
            new_task = Task.objects.create(name_of_task=name_of_task, description=description, status=status, task_data=task_data)
            return redirect("task_view", pk=new_task.pk)
        return render(request, "create.html", {"form": form})