from django.contrib.auth.models import AbstractUser
from django.db import models

from TeachingPlatform.users.managers import CustomUserManager

LESSON_TYPE = (
    ("B", "Backend"),
    ("F", "Frontend"),
    ("D", "Devops"),
    ("S", "System Administration"),
    ("C", "Cloud Engineering"),
)


class CustomUser(AbstractUser):
    email = models.EmailField("email address", unique=True)
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: list[str] = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Student(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    date_joined = models.DateField()
    email = models.EmailField(max_length=256)
    lesson_type = models.CharField(max_length=1, choices=LESSON_TYPE)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.get_lesson_type_display()}"


class Teacher(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    specialization = models.CharField(max_length=128, choices=LESSON_TYPE)
    email = models.EmailField(max_length=256)
    student = models.ManyToManyField(Student)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.get_specialization_display()}"
