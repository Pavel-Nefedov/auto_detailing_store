"""Определяет схемы URL для orders"""

from django.urls import path, re_path

from . import views

app_name = "products"
urlpatterns = [
    # Домашняя страница
    path('', views.orders, name='index'),
    # path('about', views.about, kwargs={"name":"Tom", "age": 38}),
    # path('avd', views.avd),
]