from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def contact(request):
    if request.method == 'POST':
        # Process form data
        # Example: access form fields using request.POST.get('field_name')
        # Perform necessary actions

        return render(request, 'form.html')