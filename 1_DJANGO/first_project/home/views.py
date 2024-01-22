from django.shortcuts import render
from django.http import HttpResponse
from home.models import Contact_model
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
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact_model(name = name, email = email, phone = phone, desc = desc)
        contact.save()
    else:
        return render(request, "contacts.html")
    # return HttpResponse("Contacts page")