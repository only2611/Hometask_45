from django.contrib import admin
from django.urls import path

from TO_DO_list.views import index_view, create_task

urlpatterns = [
    path("", index_view),
    path('add/', create_task)
]