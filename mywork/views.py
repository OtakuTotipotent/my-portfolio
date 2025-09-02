from django.shortcuts import render, redirect
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
    context = {"form": form}
    return render(request, "mywork/add_project.html", context)
