from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # Home page URL
    path("home/", views.home, name="home"),  # Home page URL with trailing slash
    path("contact/", views.contact, name="contact"),  # Contact page URL
    path(
        "project/<int:id>", views.project, name="project"
    ),  # Project detail page URL with dynamic ID
]
