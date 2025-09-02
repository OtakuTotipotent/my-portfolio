from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from .forms import ProjectForm
from .models import Project


class ProjectListView(ListView):
    model = Project
    context_object_name = "projects"
    template_name = "mywork/index.html"


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = "project"
    template_name = "mywork/project_detail.html"


@login_required
def add_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ProjectForm()
    return render(request, "mywork/add_project.html", {"form": form})
