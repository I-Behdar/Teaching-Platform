from django.urls import path

from schedules.views import AvailableTimesView, TeachersDetailView

urlpatterns = [
    path("teachers_detail/", TeachersDetailView.as_view(), name='teachers_detail'),
    path("time_schedules/<int:teacher_id>", AvailableTimesView.as_view(), name='availability'),
]