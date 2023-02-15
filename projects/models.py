from django.db import models

from users.models import Student, Teacher


class Project(models.Model):
    name = models.CharField(max_length=128, null=False)
    description = models.TextField()
    date_added = models.DateField()
    student = models.ManyToManyField(Student)
    teacher = models.ManyToManyField(Teacher)

    def __str__(self):
        first_teacher = self.teacher.first()
        first_student = self.student.first()
        return f"{self.name} {self.date_added} {first_student.first_name} {first_student.last_name} {first_teacher.first_name} {first_teacher.last_name}"
