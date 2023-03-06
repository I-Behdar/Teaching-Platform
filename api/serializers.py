from rest_framework import serializers

from projects.models import Project, ProjectAssignment
from schedules.models import Schedule
from subjects.models import Subject
from users.models import Student, Teacher


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'date_added', 'accepted_teachers', 'requirements')


class ProjectAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectAssignment
        fields = ('id', 'date_assigned', 'deadline', 'student', 'supervisor', 'project')


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        name = Schedule
        fields = ('id', 'start_date', 'end_date', 'teacher')


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name', 'comment']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'date_joined', 'email', 'lesson_type']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'specialization', 'email', 'student']
