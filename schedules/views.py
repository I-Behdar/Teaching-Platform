from django.shortcuts import render
from django.views import View

from schedules.models import Schedule
from users.models import Teacher


class AvailableTimesView(View):
    def get(self, request, teacher_id):
        available_times = Schedule.objects.all().filter(id=teacher_id)
        teacher = Teacher.objects.get(id=teacher_id)
        context = {'available_times': available_times, 'teacher': teacher}
        return render(request, "schedules/time_schedules.html", context)

