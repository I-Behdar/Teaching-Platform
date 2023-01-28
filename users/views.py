from django.shortcuts import render
from django.views import View

from users.models import Teacher


class HomeView(View):
    def get(self, request):
        context = {}
        return render(request, "users/home.html", context)


class TeachersView(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        context = {'teachers': teachers}
        return render(request, "users/teachers.html", context)
