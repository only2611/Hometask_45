from django.db import models

# Create your models here.

STATUS = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]

class Task(models.Model):
    description = models.CharField(max_length=100, null=False, blank=False, verbose_name="Описание задачи")
    status = models.CharField(max_length=100, choices=STATUS, verbose_name="Статус задачи", default="new")
    task_data = models.CharField(max_length=20, null=True, blank=True, verbose_name="Дата выполнения", default="")


    def __str__(self):
        return f"{self.id}. {self.description} - {self.status}"


    class Meta:
        db_table = "tasks"
        verbose_name = "задача"
        verbose_name_plural = "Задачи"