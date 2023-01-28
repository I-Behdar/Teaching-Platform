from django.urls import path

from schedules.views import AvailableTimesView

urlpatterns = [
    path("time_schedules/<int:teacher_id>", AvailableTimesView.as_view(), name='availability'),

]