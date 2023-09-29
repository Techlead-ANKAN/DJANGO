from django.http import HttpResponse

def links(request):
    return HttpResponse('''<h1> Personal Navigator </h1> 1. <a href = "https://www.1377x.to/">Link for Free Downloads </a> <br>2. <a href = "https://www.youtube.com/">Youtube </a><br>3. <a href ="https://github.com/Techlead-ANKAN">Ankan's GitHub</a><br>4. <a href = "https://mail.google.com/mail/u/0/#inbox">Ankan's Gmail</a><br>5. <a href = "https://www.hotstar.com/in/onboarding/profile?ref=%2Fin">Hotstar</a>''')
