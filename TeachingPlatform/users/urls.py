from django.urls import path

from TeachingPlatform.users.views import HomeView, TeachersView, AddTeachersView, StudentsView, DeleteStudentView, \
    DeleteTeacherView, \
    EditTeacherView, StudentsListView

urlpatterns = [
    path("", HomeView.as_view(), name='home_temp'),
    path("teachers/", TeachersView.as_view(), name='all_teachers_list'),
    path("add_teachers/", AddTeachersView.as_view(), name='teachers_add'),
    path("students/", StudentsView.as_view(), name='all_students_list'),
    path("students_list/<int:teacher_id>", StudentsListView.as_view(), name='students_list'),
    path("students_del/<int:student_id>", DeleteStudentView.as_view(), name='students_del'),
    # path("students_dash/<int:student_id>", StudentDashboardView.as_view(), name='students_dashboard'),
    path("teachers_del/<int:teacher_id>", DeleteTeacherView.as_view(), name='teachers_del'),
    path("teachers_edit/<int:teacher_id>", EditTeacherView.as_view(), name='teachers_edit'),
]
