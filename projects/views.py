from django.shortcuts import render
from django.views import View

from projects.models import Project


class ProjectsView(View):
    def get(self, request):
        projects = Project.objects.all()
        context = {'projects': projects}
        return render(request, "projects/projects_display.html", context)
