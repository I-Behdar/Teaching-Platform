from django.shortcuts import render
from django.views import View


class ProjectsView(View):
    def get(self, request):
        context = {}
        return render(request, "projects/projects_display.html", context)
