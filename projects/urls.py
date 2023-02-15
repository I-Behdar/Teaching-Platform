from django.urls import path

from projects.views import ProjectsView

urlpatterns = [
    path("projects/", ProjectsView.as_view(), name="projects_display"),
]