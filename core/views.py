from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from core.models import Bottle
from .forms import LoginForm
# core/views.py

def contacts(request):
    return render(request, 'core/contacts.html')

def about(request):
    return render(request, 'about.html')

def logout_view(request):
    logout(request)

def makers_list(request):
    context = {}
    # SELECT * FROM Botlle
    bottles_list = Bottle.objects.all()
    context["bottles_list"] = bottles_list
    return render(request, 'makers.html', context)

class LoginView(View):
    def get(self, request):
        context = {"form": LoginForm()}
        return render(request, 'auth/sign_in.html', context)

    def post(self, request, *args, **kwargs):
        data = request.POST
        user_login = data["username"]
        password = data["password"]
        user = authenticate(request, username=user_login, password=password)
        if user is not None:
            login(request, user)
            return redirect(logout)
        else:
            return HttpResponse("Неверный логин или пароль")

   

            