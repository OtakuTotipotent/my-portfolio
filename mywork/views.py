from django.shortcuts import render, redirect, get_object_or_404
from .models import Project
from .forms import ProjectForm


def index(request):
    projects = Project.objects.all()
    return render(request, "mywork/index.html", {"projects": projects})


def add_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ProjectForm()
    return render(request, "mywork/add_project.html", {"form": form})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, "mywork/project_detail.html", {"project": project})
