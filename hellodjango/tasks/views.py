from django import forms
from django.shortcuts import render

tasks = ["hey", "hello", "nice"]

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New TTask")
    priority = forms.IntegerField(label="priority", min_value=1, max_value=10)

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })