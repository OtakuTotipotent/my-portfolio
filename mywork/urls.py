# mywork/urls.py file
from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProjectListView.as_view(), name="work"),
    path("<int:pk>/", views.ProjectDetailView.as_view(), name="project-detail"),
]
