from django.shortcuts import render

tasks = ["hey", "hello", "nice"]

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        
    })
