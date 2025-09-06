# pages/ app's urls.py file
from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("ordernow/", views.OrdernowView.as_view(), name="ordernow"),
]
