from django.db import models

LESSON_TYPE = (
    ("B", "Backend Dev"),
    ("F", "Frontend Dev"),
    ("D", "Devops"),
    ("S", "System Administration"),
    ("C", "Cloud Engineering"),
)


class Student(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    date_joined = models.DateField()
    email = models.EmailField(max_length=256)
    lesson_type = models.CharField(max_length=1, choices=LESSON_TYPE)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.lesson_type}"


class Teacher(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    specialization = models.CharField(max_length=128)
    email = models.EmailField(max_length=256)
    student = models.ManyToManyField(Student)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.specialization}"
