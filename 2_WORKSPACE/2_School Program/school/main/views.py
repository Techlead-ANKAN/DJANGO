from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def image(request):
    return render(request, "image.html")


def newproject(request):
    return render(request, "newproject.html")

def home(request):
    return render(request, "home.html")

def student_reg(request):
    return render(request, "studentregistration.html")

def subject(request):
    return render(request, "subject.html")

def syllabus(request):
    return render(request, "syllabus.html")

def teachers(request):
    return render(request, "teachers.html")