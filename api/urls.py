from django.urls import path
from .views import ProjectView, ProjectAssignmentView, ScheduleSerializerView, SubjectSerializerView, \
    StudentSerializerView, TeacherSerializerView

urlpatterns = [
    path('projects', ProjectView.as_view()),
    path('projects', ProjectAssignmentView.as_view()),
    path('projects', ScheduleSerializerView.as_view()),
    path('projects', SubjectSerializerView.as_view()),
    path('projects', StudentSerializerView.as_view()),
    path('projects', TeacherSerializerView.as_view()),
]