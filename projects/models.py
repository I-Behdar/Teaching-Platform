from django.db import models

from subjects.models import Subject
from users.models import Student, Teacher


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
    date_assigned = models.DateTimeField()
    deadline = models.DateTimeField()
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    supervisor = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    project = models.ManyToManyField(Project) # needs to check if manytomany or other relations

    def __str__(self):
        first_project = self.project.first()
        return f"{first_project.name} {self.student} {self.supervisor} {self.date_assigned} {self.deadline}"
