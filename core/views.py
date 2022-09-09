from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import View, CreateView
from django.contrib.auth import authenticate, login, logout
from core.models import Bottle
from .forms import LoginForm, UserRegistrationForm
# core/views.py

def contacts(request):
    return render(request, 'core/contacts.html')

def about(request):
    return render(request, 'about.html')

def LogoutView(request):
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
            return redirect(about)
        else:
            return HttpResponse("Неверный логин или пароль")


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'auth/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'auth/register.html', {'user_form': user_form})



