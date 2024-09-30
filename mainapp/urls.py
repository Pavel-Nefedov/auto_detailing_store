"""Определяет схемы URL для mainapp"""

from django.urls import path, re_path

from . import views

app_name = "mainapp"
urlpatterns = [
    # Домашняя страница
    re_path(r'^$', views.category_list, name='category_list'),
]