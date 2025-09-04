from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProjectListView.as_view(), name="index"),
    path("<int:pk>/", views.ProjectDetailView.as_view(), name="project-detail"),
]
