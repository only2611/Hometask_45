from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


# Create your views here.
from TO_DO_list.models import STATUS, Task


def index_view(request):
    tasks = Task.objects.all()
    context = {"tasks": tasks}
    return render(request, "index.html", context)

def task_view(request):
    pass


def create_task(request):
    if request.method == "GET":
        return render(request, "create.html", {"statuses": STATUS})
    else:
        description = request.POST.get("description")
        status =  request.POST.get("status")
        task_data = request.POST.get("task_data")
        new_task = Task.objects.create(description=description, status=status, task_data=task_data)
        context = {"task": new_task}
        return render(request, "task.html", context)