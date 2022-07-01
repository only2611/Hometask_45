from django import forms
from django.forms import widgets

STATUS = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]

class TaskForm(forms.Form):
    name_of_task = forms.CharField(max_length=100, required=True, label='name_of_task')
    description = forms.CharField(max_length=100, required=True, label='description')
    status = forms.ChoiceField(choices=STATUS, widget=widgets.Select, required=True, label='status')
    task_data = forms.CharField(max_length=20, required=True, label='task_data')
