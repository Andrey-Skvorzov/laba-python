from django.http import HttpResponse
from django.shortcuts import render

def index(request): #index имя можно менять request обращается к запросу
    return HttpResponse("Страница приложения mail.")
# Create your views here.
