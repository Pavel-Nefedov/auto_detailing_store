from django.shortcuts import render
from django.http import HttpResponse


def orders(request):
    return render(request, '../templates/orders.html')  #путь к нужному шаблону
