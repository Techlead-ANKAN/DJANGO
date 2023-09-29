from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
    # return HttpResponse("<h1>HOME</h1>")

def analyze(request):
    # getting the text
    print(request.GET.get("text", "off"))
    print(request.GET.get("remove_punc", "off"))
    return HttpResponse('''<h1>Remove Punctuation</h1><a href = "http://127.0.0.1:8000/">Back</a>''')

# def cap_first(request):
#     return HttpResponse('''<h1>Capitalize First</h1><a href = "http://127.0.0.1:8000/remove_punc">Back</a>''')

# def remove_space(request):
#     return HttpResponse('''<h1>Remove Space</h1><a href = "http://127.0.0.1:8000/cap_first">Back</a>''')

# def new_lineremove(request):
#     return HttpResponse('''<h1>Remove New Line</h1><a href = "http://127.0.0.1:8000/space_remove">Back</a>''')

# def char_count(request):
#     return HttpResponse('''<h1>Count Characters</h1><a href = "http://127.0.0.1:8000/new_line_remove">Back</a>''')