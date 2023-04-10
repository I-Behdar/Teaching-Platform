from django.urls import path

from TeachingPlatform.projects.views import ProjectsView

urlpatterns = [
    path("projects/", ProjectsView.as_view(), name="projects_display"),
]