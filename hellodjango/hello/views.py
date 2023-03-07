from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello!")

def yasin(request):
    return HttpResponse("Hello, Yasin")

def greet(request, name):
    return HttpResponse(f"hello, {name}")