from rest_framework import generics

from schedules.models import Schedule
from projects.models import Project, ProjectAssignment
from subjects.models import Subject
from users.models import Student, Teacher

from .serializers import ProjectSerializer, ProjectAssignmentSerializer, ScheduleSerializer, SubjectSerializer, \
    StudentSerializer, TeacherSerializer


class ProjectView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectAssignmentView(generics.ListAPIView):
    queryset = ProjectAssignment.objects.all()
    serializer_class = ProjectAssignmentSerializer


class ScheduleSerializerView(generics.ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class SubjectSerializerView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class StudentSerializerView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherSerializerView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
