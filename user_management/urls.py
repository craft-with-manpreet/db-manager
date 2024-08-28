# Author: Manpreet Singh
# Email: dev.manpreet.io@gmail.com
# GitHub: https://github.com/craft-with-manpreet
# Portfolio: https://dev-manpreet.web.app
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('logout', views.logout, name="logout")
]
