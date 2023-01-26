from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self, request):
        context = {}
        return render(request, "users/home.html", context)
