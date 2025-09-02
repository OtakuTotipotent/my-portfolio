from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProjectListView.as_view(), name="index"),
    path("add/", views.add_project, name="add-project"),
    path("<int:pk>/", views.ProjectDetailView.as_view(), name="project-detail"),
]
