"""Определяет схемы URL для authapp"""
from django.urls import path
import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login, name='login'),
    path('logout/', authapp.logout, name='logout'),
    path('register/', authapp.register, name='register'),
    path('edit/', authapp.edit, name='edit'),
    path('message/', authapp.message, name='message'),
    path('verify/<str:email>/<str:activation_key>/', authapp.verify, name='verify'),
]