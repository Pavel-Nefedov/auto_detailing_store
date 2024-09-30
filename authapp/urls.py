"""Определяет схемы URL для authapp"""
from django.contrib.auth import views
from django.urls import path
from authapp import views

app_name = 'authapp'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    # path('login/', views.LoginUser.as_view(), name='login'),
    # path('register/', views.RegisterUser.as_view(), name='register'),
    # path('login_success/', views.SuccessLogin.as_view(), name='login_success'),
    # path('logout/', views.LogoutUser.as_view(), name='logout')

]