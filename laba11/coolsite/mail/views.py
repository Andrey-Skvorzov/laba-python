from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


# Create your views here.
def index(request): #index имя можно менять request обращается к запросу
    return HttpResponse("Страница приложения mail.")

def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
