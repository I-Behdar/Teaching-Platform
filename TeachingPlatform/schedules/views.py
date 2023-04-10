from django.shortcuts import render
from django.views import View

from TeachingPlatform.schedules.models import Schedule
from TeachingPlatform.users.models import Teacher


class TeachersDetailView(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        context = {'teachers': teachers}
        return render(request, "schedules/teachers_detail.html", context)


class AvailableTimesView(View):
    def get(self, request, teacher_id):
        available_times = Schedule.objects.filter(teacher=teacher_id)
        teacher = Teacher.objects.get(id=teacher_id)
        context = {'available_times': available_times, 'teacher': teacher}
        return render(request, "schedules/time_schedules.html", context)
