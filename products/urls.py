"""Определяет схемы URL для products"""

from django.urls import path, re_path

from .views import products, product

app_name = "products"

urlpatterns = [
    path('', products, name='index'),
    path('category/<int:pk>/', products, name='category'),
    path('product/<int:pk>/', product, name='detail'),
    path('category/<int:pk>/page/<int:page>/', products, name='page'),
]

# urlpatterns = [
#     # Домашняя страница
#     path('', views.catalog, name='index'),
# ]
