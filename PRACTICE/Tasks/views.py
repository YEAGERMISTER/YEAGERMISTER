from django.shortcuts import render
from django import forms
from django.forms import NewTaskForm
from django.http import HttpResponse

# Create your views here.
tasks = ["Laundry", "Shopping", "Cleaning"]

def index(request):
    return render(request, "Tasks/index.html", {
        "tasks": tasks
    }) 

def add(request):
    if request.method == "Post":
        form = NewTaskForm(request.Post)
        if form.is_valid():
            form.cleaned_data["task"]
            tasks.append()

    return render(request, "Tasks/add.html",{
        "form": forms.NewTaskForm()
    })

