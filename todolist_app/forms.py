from django import forms
from .models import TaskList
class taskForm(forms.ModelForm):
    """Form definition for task."""

    class Meta:
        """Meta definition for taskform."""

        model = TaskList
        fields = ['task','done']

