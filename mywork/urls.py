from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_project, name="add-project"),
    path("<int:pk>/", views.project_detail, name="project-detail"),
]
