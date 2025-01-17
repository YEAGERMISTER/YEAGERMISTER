from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "Hello/ind.html")

def greet(request, name):
    return render(request, "Hello/greet.html",{
        "name" : name.capitalize()
    })