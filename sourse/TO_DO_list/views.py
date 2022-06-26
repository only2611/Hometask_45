from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


# Create your views here.
def index_view(request):
    query = request.GET.getlist("name", "rrrrrrrrrrr")
    print(query)
    context = {"name": "Need", "test": "Python"}
    return render(request, "index.html", context)


def create_article(request):
    if request.method == "GET":
        return render(request, "create.html")
    else:
        user =  {
            "name": "Test",
            "age": 25,
            "email": "loet@inbox.ru"
        }
        context = {
            "title": request.POST.get("title"),
            "author": request.POST.get("author"),
            "content": request.POST.get("content"),
            "user": user,

        }
        return render(request, "article_view.html", context)