from django.shortcuts import render
from django import forms
from django.http import HttpResponse

# Create your views here.
tasks = ["Laundry", "Shopping", "Cleaning"]

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)
 
def index(request):
    return render(request, "Tasks/index.html", {
        "tasks": tasks
    }) 

def add(request):

    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)     
        else:
            return render(request, "Tasks/add.html", {
                "form": form
            })
    return render(request, "Tasks/add.html",{
        "form": NewTaskForm()
    })

