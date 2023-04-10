from django.urls import path
from .views import ProjectView, ProjectAssignmentView, ScheduleSerializerView, SubjectSerializerView, \
    StudentSerializerView, TeacherSerializerView

urlpatterns = [
    path('projects', ProjectView.as_view()),
    path('projectassignment', ProjectAssignmentView.as_view()),
    path('schedule', ScheduleSerializerView.as_view()),
    path('subject', SubjectSerializerView.as_view()),
    path('student', StudentSerializerView.as_view()),
    path('teacher', TeacherSerializerView.as_view()),
]