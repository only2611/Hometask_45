from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.shortcuts import render


# Create your views here.
from TO_DO_list.models import STATUS, Task


def index_view(request):
    tasks = Task.objects.all()
    context = {"tasks": tasks}
    return render(request, "index.html", context)

def task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, "task.html", {"task": task})


def create_task(request):
    if request.method == "GET":
        return render(request, "create.html", {"statuses": STATUS})
    else:
        name_of_task = request.POST.get("name_of_task")
        description = request.POST.get("description")
        status =  request.POST.get("status")
        task_data = request.POST.get("task_data")
        new_task = Task.objects.create(name_of_task=name_of_task, description=description, status=status, task_data=task_data)
        return redirect("task_view", pk=new_task.pk)