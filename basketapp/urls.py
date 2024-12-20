"""Определяет схемы URL для mainapp"""

from django.urls import path, re_path

import basketapp.views as basketapp

app_name = "basketapp"
urlpatterns = [
    path('', basketapp.basket, name='index'),
    path('add/<int:pk>/', basketapp.basket_add, name='add'),
    path('remove/<int:pk>/', basketapp.basket_remove, name='remove'),
    path('edit/<int:pk>/<int:quantity>/', basketapp.basket_edit, name='edit')
]