"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views

admin.site.site_header = "Ankan's Portfolio Admin Page"
admin.site.site_title = "Ankan's Portfolio"
admin.site.index_title = "Welcome to Ankan's Portfolio"

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name = "Home"),  
    path('login', views.login, name = "Login"),
    path('about', views.about, name = "About Me"),
    path('resources', views.resources, name = "Resources"),
    path('contact', views.contact, name = "Contact Me"),
    path('repositories', views.repositories, name = "Repositories"),
    path('zip_files', views.zip_files, name = "Zip Files"),
    path('signup', views.signup, name = "Sign up")
]
