from django.forms import ModelForm, TextInput, CheckboxInput
from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['task', 'completed']
        widgets = {
            'task': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter todo e.g. Delete junk files',
                                     'aria-label': 'Todo', 'aria-describedby': 'add-btn'}),
            'completed':CheckboxInput(attrs={'class': 'form-check-input', 'id': "flexCheckDefault"})
        }

