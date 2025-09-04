from django.views.generic import ListView, DetailView
from .models import Project


class ProjectListView(ListView):
    model = Project
    context_object_name = "projects"
    template_name = "mywork/index.html"


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = "project"
    template_name = "mywork/project_detail.html"
