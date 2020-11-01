from .models import Task
from django.forms import ModelForm, TextInput, Textarea, CheckboxInput


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        exclude = ["is_done", "author"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Input title'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Input description'
            }),
        }


class IsDoneTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["is_done"]
        exclude = ["title", "task", "author"]
        widgets = {
            "is_done": CheckboxInput(attrs={
                'onclick': 'make_line_through()',
                'name': 'check',
            }),
        }
