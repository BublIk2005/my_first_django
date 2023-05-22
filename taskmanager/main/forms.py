from .models import Task, newTask
from django.forms import ModelForm, TextInput, Textarea, DateInput

class TaskForm(ModelForm):
    class Meta:
        model = newTask
        fields = ["title", "task", "creation_date", "end_date"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите название"
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Введите описание"
            }),
            "creation_date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите срок окончания задачи"
            }, format='YYYY-MM-DD'),
            "end_date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите срок окончания задачи"
            }, format='YYYY-MM-DD')
            }
