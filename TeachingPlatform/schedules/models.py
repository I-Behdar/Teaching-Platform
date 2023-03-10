from django.db import models

from TeachingPlatform.users.models import Teacher


class Schedule(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.teacher.first_name} {self.teacher.last_name}, {self.start_date} {self.end_date}"
