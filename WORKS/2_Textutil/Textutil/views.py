# created by me 

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello User")

def about(request):
    return HttpResponse("<h1>About Website</h1>")

def display(request):
    with open("1.txt", "r") as file:
        return HttpResponse(file.read())