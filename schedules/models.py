from django.db import models

from users.models import Teacher


class Schedule(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    teacher = models.ManyToManyField(Teacher)

    def __str__(self):
        first_teacher = self.teacher.first()
        return f"{first_teacher.first_name} {first_teacher.last_name}, {self.start_date} {self.end_date}"
