from django.shortcuts import render, redirect
from django.views import View

from TeachingPlatform.users.models import Teacher, Student


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
        specialization = request.POST.get("techs")

        if Teacher.objects.filter(email=email).first():
            return render(request, "users/add_teachers.html", context={"error": "Email already exists!"})

        Teacher.objects.create(first_name=first_name, last_name=last_name, email=email, specialization=specialization)

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


class StudentsListView(View):
    def get(self, request, teacher_id):
        teacher = Teacher.objects.get(id=teacher_id)
        students = teacher.student_rel.all()
        context = {'teacher': teacher, 'students': students}
        return render(request, 'users/students_list.html', context)


class DeleteStudentView(View):
    def get(self, request, student_id):
        student = Student.objects.get(id=student_id)
        student.delete()
        return redirect('students_list')


class EditTeacherView(View):
    def get(self, request, teacher_id):
        teacher = Teacher.objects.get(id=teacher_id)
        context = {'teacher': teacher}
        return render(request, "users/edit_teacher.html", context)

    def post(self, request, teacher_id):
        teacher = Teacher.objects.get(id=teacher_id)

        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        specialization = request.POST.get("techs")

        teacher.first_name = first_name
        teacher.last_name = last_name
        teacher.specialization = specialization
        teacher.save()

        return redirect('teachers_list')


# class StudentDashboardView(View):
#     def get(self, request, student_id):
#         students = Student.objects.get(id=student_id)
#         context = {'students': students}
#         return render(request, "users/students_dashboard.html", context)