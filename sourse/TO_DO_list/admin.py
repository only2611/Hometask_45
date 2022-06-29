from django.contrib import admin

# Register your models here.
from TO_DO_list.models import Task

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','name_of_task', 'description', 'status', 'task_data',]
    list_display_links = ['description']
    list_filter = ['status']
    search_fields = ['description', 'status']
    fields = ['name_of_task', 'description', 'status', 'task_data']


admin.site.register(Task,  ArticleAdmin)