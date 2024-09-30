from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView


# class LoginUser(LoginView):
#     return render(request, '../templates/login.html') #здесь путь к нужному шаблону

# class LogoutUser(LogoutView):
#     next_page = 'auth/login'