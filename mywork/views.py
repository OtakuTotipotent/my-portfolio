from django.shortcuts import render
from .models import Project


def index(request):
    projects = Project.objects.all()
    context = {"Projects": projects}
    return render(request, "mywork/index.html", context)
