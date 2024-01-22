# created by me
from django.http import HttpResponse
from django.shortcuts import render

def index(request):    
    return render (request, 'index.html')
    # return HttpResponse ("HELLO")

def analyze(request):
    given_txt = (request.GET.get('text', 'default'))
    punc_removal = (request.GET.get('rmpunc', 'off'))
    cap_first = (request.GET.get('capfirst', 'off'))
    rm_ln = (request.GET.get('rmline', 'off'))
    rm_space = (request.GET.get('rmspace', 'off'))
    char_count = (request.GET.get('char_count', 'off'))


    analyzed_txt = ""

    if punc_removal.lower == "on":
        for i in given_txt:
            if i.isalpha() or i.isdigit() or i == " " :
                analyzed_txt += i
    elif punc_removal.lower == "off":
        analyzed_txt = given_txt
    
    if cap_first.lower == "on":
        analyzed_txt.capitalize()
    elif cap_first.lower == "off":
        analyzed_txt = analyzed_txt

    var_dict = {"your_text" : given_txt, "one" : punc_removal, "two" : cap_first, "three": rm_ln, "four" : rm_space, "five" : char_count, "analyzed_txt": analyzed_txt}
    
    return render(request, "analyze.html", var_dict)

# def capitalize_first(request):
#     return HttpResponse("CAPITALIZE FIRST")

# def line_remove(request):
#     return HttpResponse("LINE REMOVE")

# def space_remove(request):
#     return HttpResponse("SPACE REMOVE")

# def character_count(request):
#     return HttpResponse("CHARACTER COUNT")