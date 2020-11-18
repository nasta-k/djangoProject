from .models import Task
from django.forms import ModelForm, TextInput, Textarea


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
