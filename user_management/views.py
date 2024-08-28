# Author: Manpreet Singh
# Email: dev.manpreet.io@gmail.com
# GitHub: https://github.com/craft-with-manpreet
# Portfolio: https://dev-manpreet.web.app

from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from user_management.forms import LoginForm
from typing import Type
from database_management.scheduler import scheduler_instance, get_trigger


def login(request):
    template_name = "authentication/login.html"
    if request.method == "GET":
        form: LoginForm = LoginForm()
        return render(request, template_name, {"form": form})

    form: LoginForm = LoginForm(data=request.POST)
    if not form.is_valid():
        return render(request, template_name, {"form": form})

    email: str = form.cleaned_data["email"]
    user: Type[User] = User.objects.get(username=email)

    # Generating session
    auth.login(request, user)
    return redirect("database-list")


def logout(request):
    auth.logout(request)
    return redirect("login")
