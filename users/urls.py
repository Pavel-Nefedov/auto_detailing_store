"""Определяет схемы URL для users"""

from django.urls import path, re_path

from . import views

app_name = "products"
urlpatterns = [
    # Домашняя страница
    path('', views.catalog, name='index'),
    # path('about', views.about, kwargs={"name":"Tom", "age": 38}),
    # path('avd', views.avd),
]