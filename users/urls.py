from django.urls import path

from users.views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name='home'),
]
