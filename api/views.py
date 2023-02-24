from django.shortcuts import render
from rest_framework import generics

from .serializers import ProjectSerializer

from projects.models import Project, ProjectAssignment

# Create your views here.

class RoomView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer