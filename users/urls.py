from django.urls import path

from users.views import HomeView, TeachersView

urlpatterns = [
    path("", HomeView.as_view(), name='home_temp'),
    path("teachers/", TeachersView.as_view(), name='teachers_temp'),
]
