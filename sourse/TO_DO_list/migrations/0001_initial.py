# Generated by Django 4.0.5 on 2022-06-26 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Описание задачи')),
                ('status', models.CharField(choices=[('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')], default='new', max_length=100, verbose_name='Статус задачи')),
                ('task_data', models.DateField(verbose_name='Дата выполнения')),
            ],
            options={
                'verbose_name': 'задача',
                'verbose_name_plural': 'Задачи',
                'db_table': 'tasks',
            },
        ),
    ]
