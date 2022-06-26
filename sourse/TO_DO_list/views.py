from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


# Create your views here.
from TO_DO_list.models import STATUS


def index_view(request):
    query = request.GET.getlist("name", "rrrrrrrrrrr")
    print(query)
    context = {"name": "Need", "test": "Python"}
    return render(request, "index.html", context)


def create_task(request):
    if request.method == "GET":
        return render(request, "create.html", {"statuses": STATUS})
    # else:
    #     context = {
    #         "title": request.POST.get("title"),
    #         "author": request.POST.get("author"),
    #         "content": request.POST.get("content"),
    #
    #     }
    #     return render(request, "article_view.html", context)