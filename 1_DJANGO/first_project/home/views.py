from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# 1) return string: syntax --> return HttpResponse("string to display")
# 2) rendering template: syntax --> return render (request, <template_name>)  

# 3) sending variables to template from views
# context = {"variable_name" : "variable_value"}
# return render(request, "<template_name>", context)

def home(request):
    context = { "name" : "Ankan Maity" , "age" : 20}
    return render(request, "index.html", context)
    # return HttpResponse("Home Page")


def about(request):
    return render(request, "about.html")
    return HttpResponse("About Page")

def services(request):
    return render(request, "services.html")
    return HttpResponse("Service page")

def contacts(request):
    return render(request, "contacts.html")
    return HttpResponse("Contacts page")