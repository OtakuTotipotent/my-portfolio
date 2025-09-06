# mywork/forms.py
from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "image",
            "project_url",
            "github_url",
        ]
