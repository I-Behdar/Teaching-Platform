from django.contrib import admin

from TeachingPlatform.users.models import Student, Teacher, CustomUser

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(CustomUser)
