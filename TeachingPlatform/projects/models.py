from django.db import models

from TeachingPlatform.subjects.models import Subject
from TeachingPlatform.users.models import Student, Teacher


class Project(models.Model):
    name = models.CharField(max_length=128, null=False) # null necessary?
    description = models.TextField()
    date_added = models.DateField()
    accepted_teachers = models.ManyToManyField(Teacher)
    requirements = models.ManyToManyField(Subject)

    def __str__(self):
        first_teacher = self.accepted_teachers.first()
        first_requirements = self.requirements.first()
        return f"{self.name} {self.date_added} {first_teacher.first_name} " \
               f"{first_teacher.last_name} {first_requirements.name}"


class ProjectAssignment(models.Model):
    date_assigned = models.DateField()
    deadline = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    supervisor = models.ManyToManyField(Teacher)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        first_supervisor = self.supervisor.first()
        return f"{self.project.name} {self.student} {first_supervisor.first_name} {first_supervisor.last_name} {self.date_assigned} {self.deadline}"
