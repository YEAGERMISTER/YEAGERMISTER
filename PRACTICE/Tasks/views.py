from django.shortcuts import render

# Create your views here.
tasks = ["Laundry", "Shopping", "Cleaning"]

def index(request):
    return render(request, "Tasks/index.html", {
        "tasks": tasks
    }) 

def add(request):
    return render(request, "Tasks/add.html")