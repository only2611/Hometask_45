# Generated by Django 4.0.5 on 2022-06-28 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TO_DO_list', '0002_alter_task_task_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='name_of_task',
            field=models.CharField(default='python_task', max_length=100, verbose_name='Название задачи'),
        ),
    ]
