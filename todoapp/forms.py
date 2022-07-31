from django.forms import ModelForm
from django.forms import ModelForm
from .models import *


class TodoForm(ModelForm):
    class Meta:
        model = ToDo
        fields = ['title', 'memo', 'important']
