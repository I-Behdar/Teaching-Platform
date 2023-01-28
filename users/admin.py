from django.contrib import admin

from users.models import Student, Teacher

admin.site.register(Student)
admin.site.register(Teacher)
