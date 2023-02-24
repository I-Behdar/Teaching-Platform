from rest_framework import serializers

from projects.models import Project, ProjectAssignment
from schedules.models import Schedule
from subjects.models import Subject
from users.models import Student, Teacher

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'date_added', 'accepted_teachers', 'requirements')

