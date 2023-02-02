from django.shortcuts import render, redirect
from django.views import View

from users.models import Teacher, Student


class HomeView(View):
    def get(self, request):
        context = {}
        return render(request, "users/home.html", context)


class TeachersView(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        context = {'teachers': teachers}
        return render(request, "users/teachers.html", context)


class AddTeachersView(View):
    def get(self, request):
        context = {}
        return render(request, "users/add_teachers.html", context)

    def post(self, request):
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")

        Teacher.objects.create(first_name=first_name, last_name=last_name, email=email)

        return redirect('teachers_list')


class DeleteTeacherView(View):
    def get(self, request, teacher_id):
        teacher = Teacher.objects.get(id=teacher_id)
        teacher.delete()
        return redirect('teachers_list')


class StudentsView(View):
    def get(self, request):
        students = Student.objects.all()
        context = {'students': students}
        return render(request, "users/students.html", context)


class DeleteStudentView(View):
    def get(self, request, student_id):
        student = Student.objects.get(id=student_id)
        student.delete()
        return redirect('students_list')

#
# class DeleteTeachersView(View):
#     def get(self, request):
#         context = {}
#         return render(request, "users/add_students.html", context)
#
#     def post(self, request):
#         first_name = request.POST.get("first_name")
#         last_name = request.POST.get("last_name")
#         email = request.POST.get("email")
#
#         Teacher.objects.create(first_name=first_name, last_name=last_name, email=email)
#
#         return redirect('teachers_temp')
