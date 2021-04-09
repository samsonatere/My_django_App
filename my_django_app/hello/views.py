from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello World!")

def samson(request):
    return HttpResponse("Hello, Samson!")

def atere(request):
    return HttpResponse("Hello, Atere!")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")