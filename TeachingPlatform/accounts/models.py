from django.db import models

from TeachingPlatform.users.models import Student, Teacher


# class AbstractAccount(models.Model):
#     user = models.OneToOneField(Student/Teacher???, on_delete=models.CASCADE, primary_key=True)
# 1. Is it good practice to make an abstract model to inherit from since we will have 2 field-simillar accounts?
# 2. When do we specify 'primary_key=True', is it mandatory to specify it?
#     date_created = models.DateTimeField(verbose_name="date created", auto_now_add=True)
# 1. We have date_joined in Student model, do we need a date_created for the account?
#     class Meta:
#         abstract = True


class StudentAccount(models.Model):
    user_student = models.OneToOneField(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_student}"


class TeacherAccount(models.Model):
    user_teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_teacher}"
