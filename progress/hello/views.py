from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello Issah")

def Issah(request):
    return HttpResponse("Keep on going, my first django program written by myself.")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")