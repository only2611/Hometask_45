from django.contrib import admin
from django.urls import path

from TO_DO_list.views import index_view, create_task, task_view

urlpatterns = [
    path("", index_view, name="index_view"),
    path('add/', create_task, name="create_task"),
    path('task/<int:pk>/', task_view, name="task_view"),
]