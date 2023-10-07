from django import forms
from .models import Project

class ProjectForm(forms.Form):
    name = forms.CharField(max_length=200)