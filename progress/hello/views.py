from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get("name", "World") # Default to "World" if name is not provided
        return HttpResponseRedirect(reverse("greet", args=[name]))
    else:
        return render(request, "hello/index.html")


def Issah(request):
    return HttpResponse("Keep on going, my first django program written by myself.")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })