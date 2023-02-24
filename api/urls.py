from django.urls import path
from .views import RoomView

urlpatterns = [
    path('projects', RoomView.as_view()),
]