from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=128)
    comments = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.comments}"
