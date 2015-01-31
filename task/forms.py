from django import forms

from task.models import TaskComments


class TaskCommentsForm(forms.ModelForm):
    class Meta:
        model = TaskComments
        fields = ['tcomments']