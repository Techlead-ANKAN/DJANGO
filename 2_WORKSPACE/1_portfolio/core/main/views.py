from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html")
    # return HttpResponse("This is the Home page.")

def login(request):
    return render(request, "login.html")
    return HttpResponse("This is Login Page.")

def resources(request):
    return render(request, "resources.html")
    # return HttpResponse("Resources available.")

def repositories(request):
    return render(request, "repositories.html")
    # return HttpResponse("Available Repositories.")

def zip_files(request):
    return render(request, "zip_files.html")
    # return HttpResponse("Available Repositories.")

def about(request):
    return render(request, "about.html")
    # return HttpResponse("This page is about me.")

def contact(request):
    return render(request, "contact.html")
    # return HttpResponse("This page is for contacting me.")

def signup(request):
    return render(request, "signup.html")
    # return HttpResponse("This page is for contacting me.")
